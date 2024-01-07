from bson import ObjectId
from pymongo import MongoClient
from dto.product_dto import ProductDTO  # Ensure this import path is correct based on your project structure
from db.db_connection import DBConnection  # Ensure this import path is correct based on your project structure

class ProductDAO:
    def __init__(self, db_connection):
        self.db = db_connection.get_db()  # Assumes db_connection is an instance of your DBConnection class

    def create_product(self, product_dto):
        # Convert ProductDTO to dictionary and insert into the database
        product_data = product_dto.__dict__
        return self.db.Products.insert_one(product_data).inserted_id

    def get_product_by_id(self, product_id):
        return self.db.Products.find_one({"_id": ObjectId(product_id)})

    def update_product(self, product_id, update_data):
        # Update product document with the provided update_data dictionary
        return self.db.Products.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})

    def delete_product(self, product_id):
        return self.db.Products.delete_one({"_id": ObjectId(product_id)})

    def list_all_products(self):
        return list(self.db.Products.find({}))

# Example Usage
# You would usually not run this here but in your main application logic
if __name__ == "__main__":
    db_uri = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
    db_name = "EtsyProducts"  # Replace with your database name
    db_conn = DBConnection(db_uri)  # Make sure to import and correctly initialize your DBConnection class
    db_conn.connect(db_name)

    product_dao = ProductDAO(db_conn)

    # Example of creating a new product
    new_product = ProductDTO(
        # populate with product details
    )
    print("New Product ID:", product_dao.create_product(new_product))

    # Fetching a product
    print("Product Details:", product_dao.get_product_by_id("some_product_id"))
