# models/product.py

class Product:
    def __init__(self, product_id, title, description, price, tags, url):
        self.product_id = product_id
        self.title = title
        self.description = description
        self.price = price  # This can be a float or a dictionary with currency
        self.tags = tags  # List of strings representing tags
        self.url = url  # URL to the product's page

    # Add methods related to product behavior, if any, like updating price or description
