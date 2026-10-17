from pricing import calculate_total


def checkout(unit_prices: list[float]) -> str:
    total = calculate_total(unit_prices)
    return f"${total:.2f}"
