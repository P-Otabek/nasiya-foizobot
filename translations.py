# translations.py
translations = {
    "ask_currency": {
        "en": "💱 Choose the currency:",
        "uz": "💱 Valyutani tanlang:",
        "ru": "💱 Выберите валюту:"
    },
    "usd_disclaimer": {
        "en": "⚠️ Interest rates in US dollars cannot be directly compared to microloan interest rates in Uzbek soums. Although the rate turns out to be lower, it can be higher due to the exchange rate difference.",
        "uz": "⚠️ AQSH dollaridagi foiz stavkalarni O‘zbek so‘midagi mikroqarz foiz stavkalariga to‘g‘ridan-to‘g‘ri solishtirib bo‘lmaydi. Stavka kichikroq chiqsa-da, valyuta kursdagi farq tufayli balandroq bo‘lishi mumkin.",
        "ru": "⚠️ Процентные ставки в долларах США не могут быть напрямую сопоставлены с процентными ставками по микрозаймам в узбекских сумах. Хотя ставка может быть меньше, она может быть выше из-за разницы в обменном курсе."
    },
    "ask_cash_price": {
        "en": "💰 Enter the cash (full) price:",
        "uz": "💰 Mahsulotning naqd (to‘liq) narxini kiriting:",
        "ru": "💰 Введите полную (наличную) цену товара:"
    },
    "ask_payment": {
        "en": "💳 Enter the regular payment amount:",
        "uz": "💳 Har bir davriy to‘lov miqdorini kiriting:",
        "ru": "💳 Введите сумму регулярного платежа:"
    },
    "ask_num_periods": {
        "en": "⏱️ Enter the number of periods/payments:",
        "uz": "⏱️ To‘lovlar sonini kiriting:",
        "ru": "⏱️ Введите количество платежей:" 
    },
    "ask_period_type": {
        "en": "📅 Choose the payment frequency:",
        "uz": "📅 To‘lovlar davriyligini tanlang:",
        "ru": "📅 Выберите периодичность платежей:"
    },
    "invalid_input": {
        "en": "⚠️ Invalid input. Please enter a number.",
        "uz": "⚠️ Noto‘g‘ri kiritma. Iltimos, raqam kiriting.",
        "ru": "⚠️ Неверный ввод. Пожалуйста, введите число."
    },
    "result": {
        "en": "Here is your BNPL summary:",
        "uz": "Nasiya hisob-kitob natijasi:",
        "ru": "Результаты рассрочки:"
    },
    "verdict_cheap": {
        "en": "✅ This is cheaper than typical bank loans.",
        "uz": "✅ Bu bank kreditlariga qaraganda arzonroq variant.",
        "ru": "✅ Это дешевле, чем обычный банковский кредит."
    },
    "verdict_normal": {
        "en": "⚖️ This is similar to bank loan rates.",
        "uz": "⚖️ Bu bank kreditlari darajasiga yaqin.",
        "ru": "⚖️ Это примерно на уровне банковских кредитов."
    },
    "verdict_expensive": {
        "en": "❗ This is MUCH more expensive than bank loans.",
        "uz": "❗ Bu bank kreditlariga qaraganda ANCHA qimmatroq.",
        "ru": "❗ Это ГОРАЗДО дороже, чем банковские кредиты."
    },
    "apr_explanation": {
        "en": (
            "📘 *What do the rates mean?*\n\n"
            "🔹 *Nominal APR*: A simple annual interest rate without compounding. Useful for comparing to microloans.\n\n"
            "🔹 *Effective APR*: Includes the effect of compounding. Reflects the true cost.\n"
            "The more frequent the payments, the higher the effective rate tends to be."
        ),
        "uz": (
            "📘 *Foiz stavkalari nimani anglatadi?*\n\n"
            "🔹 *Nominal stavka* – bu yillik oddiy foiz stavkasi. Bu ko‘rsatkich bank mikroqarzlari bilan solishtirish uchun qulay.\n\n"
            "🔹 *Effektiv stavka* – murakkab foizlarni hisobga oladi va asl xarajatni ko‘rsatadi.\n"
            "To‘lovlar qanchalik tez-tez bo‘lsa, effektiv stavka shunchalik yuqori bo‘ladi."
        ),
        "ru": (
            "📘 *Что означают ставки?*\n\n"
            "🔹 *Номинальная ставка* – простая годовая ставка, без учета сложных процентов. Удобно для сравнения с банковскими кредитами.\n\n"
            "🔹 *Эффективная ставка* – учитывает сложные проценты и показывает реальную стоимость рассрочки.\n"
            "Чем чаще платежи, тем выше эффективная ставка."
        )
    },
    "period_options": {
        "en": [["monthly", "weekly"], ["bi-weekly", "quarterly"]],
        "uz": [["oylik", "haftalik"], ["har ikki haftada", "choraklik"]],
        "ru": [["ежемесячно", "еженедельно"], ["раз в 2 недели", "ежеквартально"]]
    },
    "period_map": {
        "en": {
            "monthly": "monthly",
            "weekly": "weekly",
            "bi-weekly": "bi-weekly",
            "quarterly": "quarterly"
        },
        "uz": {
            "oylik": "monthly",
            "haftalik": "weekly",
            "har ikki haftada": "bi-weekly",
            "choraklik": "quarterly"
        },
        "ru": {
            "ежемесячно": "monthly",
            "еженедельно": "weekly",
            "раз в 2 недели": "bi-weekly",
            "ежеквартально": "quarterly"
        }
    }
}
