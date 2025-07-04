# bot.py
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, ConversationHandler, CallbackQueryHandler, filters
)
import os
from translations import translations
from bnpl_calculator import calculate_apr

# Conversation steps
LANGUAGE, CURRENCY, CASH_PRICE, INITIAL_PAYMENT, PAYMENT, NUM_PERIODS, PERIOD_TYPE = range(7)

# Store user choices
user_lang = {}
user_currency = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🇺🇿 Uzbek", "🇷🇺 Russian", "🇬🇧 English"]]
    await update.message.reply_text(
        "🌐 Please choose your language:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return LANGUAGE

async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang[user_id] = "en"
    user_currency[user_id] = "UZS"
    context.user_data.clear()

    keyboard = [["🇺🇿 Uzbek", "🇷🇺 Russian", "🇬🇧 English"]]
    await update.message.reply_text(
        "🔄 Bot restarted. 🌐 Please choose your language:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return LANGUAGE

async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang_choice = update.message.text
    user_id = update.effective_user.id

    if "Uzbek" in lang_choice:
        user_lang[user_id] = "uz"
    elif "Russian" in lang_choice:
        user_lang[user_id] = "ru"
    else:
        user_lang[user_id] = "en"

    lang = user_lang[user_id]
    keyboard = [["UZS", "USD"]]
    await update.message.reply_text(
        translations['ask_currency'][lang],
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return CURRENCY

async def choose_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    currency = update.message.text
    user_id = update.effective_user.id
    lang = user_lang.get(user_id, "en")
    user_currency[user_id] = currency

    if currency == "USD":
        await update.message.reply_text(translations['usd_disclaimer'][lang])

    await update.message.reply_text(translations['ask_cash_price'][lang])
    return CASH_PRICE

async def get_cash_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = user_lang.get(update.effective_user.id, "en")
    try:
        cash_price = float(update.message.text.replace(",", ""))
        context.user_data['cash_price'] = cash_price

        await update.message.reply_text({
            'uz': "🧾 Agar dastlabki to'lov bo‘lsa, miqdorini kiriting. Aks holda 0 deb yozing:",
            'ru': "🧾 Если был первоначальный взнос, введите сумму. Иначе введите 0:",
            'en': "🧾 If there was an initial payment, enter the amount. Otherwise enter 0:"
        }[lang])
        return INITIAL_PAYMENT
    except:
        await update.message.reply_text(translations['invalid_input'][lang])
        return CASH_PRICE

async def get_initial_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = user_lang.get(update.effective_user.id, "en")
    try:
        initial = float(update.message.text.replace(",", ""))
        context.user_data['initial_payment'] = initial
        await update.message.reply_text(translations['ask_payment'][lang])
        return PAYMENT
    except:
        await update.message.reply_text(translations['invalid_input'][lang])
        return INITIAL_PAYMENT

async def get_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = user_lang.get(update.effective_user.id, "en")
    try:
        payment = float(update.message.text.replace(",", ""))
        context.user_data['payment'] = payment
        await update.message.reply_text(translations['ask_num_periods'][lang])
        return NUM_PERIODS
    except:
        await update.message.reply_text(translations['invalid_input'][lang])
        return PAYMENT

async def get_num_periods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = user_lang.get(update.effective_user.id, "en")
    try:
        periods = int(update.message.text)
        context.user_data['num_periods'] = periods
        await update.message.reply_text(
            translations['ask_period_type'][lang],
            reply_markup=ReplyKeyboardMarkup(translations['period_options'][lang], one_time_keyboard=True, resize_keyboard=True)
        )
        return PERIOD_TYPE
    except:
        await update.message.reply_text(translations['invalid_input'][lang])
        return NUM_PERIODS

async def get_period_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = user_lang.get(update.effective_user.id, "en")
    user_id = update.effective_user.id

    raw_period = update.message.text.strip().lower()
    period_type = translations['period_map'][lang].get(raw_period, 'monthly')
    context.user_data['period_type'] = period_type

    # Collect inputs
    pv = context.user_data['cash_price'] - context.user_data.get('initial_payment', 0)
    pmt = context.user_data['payment']
    n = context.user_data['num_periods']

    try:
        nominal_rate, effective_rate = calculate_apr(pv, pmt, n, period_type)

        if nominal_rate < 30:
            verdict = translations['verdict_cheap'][lang]
        elif nominal_rate > 50:
            verdict = translations['verdict_expensive'][lang]
        else:
            verdict = translations['verdict_normal'][lang]

        summary = f"\U0001F4CA {translations['result'][lang]}\n" \
                  f"\U0001F4B8 Nominal stavka: {nominal_rate:.2f}%\n" \
                  f"\U0001F4C8 Effektiv stavka: {effective_rate:.2f}%\n" \
                  f"\n{verdict}"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("❓ Batafsil", callback_data="explain_apr")]
        ])
        await update.message.reply_text(summary, reply_markup=keyboard)
        return ConversationHandler.END
    except Exception as e:
        print("Calculation error:", e)
        await update.message.reply_text(translations['invalid_input'][lang])
        return ConversationHandler.END

async def explain_apr_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = user_lang.get(user_id, "en")

    explanation = translations['apr_explanation'][lang]
    await query.edit_message_text(text=explanation, parse_mode='Markdown')

    

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelled.")
    return ConversationHandler.END

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = user_lang.get(user_id, "en")
    await update.message.reply_markdown(translations['apr_explanation'][lang])

def main():
    TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("restart", restart)
        ],
        states={
            LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_language)],
            CURRENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_currency)],
            CASH_PRICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_cash_price)],
            INITIAL_PAYMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_initial_payment)],
            PAYMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_payment)],
            NUM_PERIODS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_num_periods)],
            PERIOD_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_period_type)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CallbackQueryHandler(explain_apr_callback, pattern="^explain_apr$"))
    

    app.run_polling()

if __name__ == "__main__":
    main()