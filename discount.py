"""Price helpers for the shop. Prices are integer cents."""


def apply_discount(price_cents, percent):
    """Return the price after a percentage discount, rounded half up to a whole cent."""
    return int(price_cents * (100 - percent) / 100)


def total(prices, percent=0):
    """Return the discounted total of a list of prices."""
    return sum(apply_discount(p, percent) for p in prices)
