import numpy_financial as npf

def calculate_apr(pv, pmt, n, period_type):
    # Cash flow: -PV now, +pmt each period
    cashflows = [-pv] + [pmt] * n

    # Internal Rate of Return (IRR per period)
    r = npf.irr(cashflows)
    if r is None:
        raise ValueError("Failed to calculate periodic rate")

    # Mapping of periods per year
    freq_map = {
        'monthly': 12,
        'weekly': 52,
        'bi-weekly': 26,
        'quarterly': 4
    }

    freq = freq_map.get(period_type.lower())
    if not freq:
        raise ValueError("Invalid period type")

    # Annual Nominal and Effective Rate
    nominal = r * freq * 100
    effective = ((1 + r) ** freq - 1) * 100

    return nominal, effective
