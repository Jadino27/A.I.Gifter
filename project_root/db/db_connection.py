from pymongo import MongoClient

class DBConnection:
    def __init__(self, uri):
        self.uri = uri
        self.client = None
        self.db = None

    def connect(self, dbname):
        try:
            # Establish a connection to the MongoDB server
            self.client = MongoClient(self.uri)
            
            # Select the specific database
            self.db = self.client[dbname]
            print(f"Connected to MongoDB database: {dbname}")

        except Exception as e:
            print(f"An error occurred while connecting to MongoDB: {e}")

    def get_db(self):
        # Return the database object
        return self.db

    def close(self):
        # Close the MongoDB connection
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
