# models/user.py

from datetime import datetime

class User:
    def __init__(self, user_id, name, email, hashed_password, address, registration_date=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.address = address  # This can be a dictionary or a separate Address class
        self.registration_date = registration_date or datetime.now()
        self.wishlist = []  # List of product_ids or Product objects
        self.confirmed_wishlist = False
        self.wishlist_expiry = None

    def add_to_wishlist(self, product_id):
        # Logic to add product to wishlist
        self.wishlist.append(product_id)

    def remove_from_wishlist(self, product_id):
        # Logic to remove product from wishlist
        self.wishlist.remove(product_id)

    def confirm_wishlist(self):
        # Logic to confirm wishlist
        self.confirmed_wishlist = True

    # ... more user behaviors like updating address, resetting password, etc.
