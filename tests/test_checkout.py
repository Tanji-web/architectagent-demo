from checkout import checkout


def test_checkout_formats_dollar_amount() -> None:
    assert checkout([12.50, 2.00]) == "$14.50"
