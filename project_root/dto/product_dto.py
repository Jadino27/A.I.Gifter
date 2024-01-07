class ProductDTO:
    def __init__(self, title, description, price, tags=None, url=None):
        self.title = title
        self.description = description
        self.price = price  # This can be a number or a dictionary including currency and amount
        self.tags = tags if tags is not None else []  # List of tags related to the product
        self.url = url  # URL to the product page or image

    def to_dict(self):
        # Convert the DTO to a dictionary, which can then be used to insert into the database
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "tags": self.tags,
            "url": self.url
        }
