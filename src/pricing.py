def calculate_total(unit_prices: list[float]) -> float:
    """Return the subtotal in cents after the seeded PR contract change."""
    return round(sum(unit_prices) * 100)
