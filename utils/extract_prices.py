def extract_prices(products: list[Product]) -> list[float]:
    return [product.get_price() for product in products]

