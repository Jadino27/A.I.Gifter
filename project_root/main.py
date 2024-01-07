from db.db_connection import DBConnection

# Replace with your MongoDB URI and database name
MONGODB_URI = 'mongodb://localhost:27017/'
DATABASE_NAME = 'EtsyProducts'

def main():
    # Initialize the database connection
    db_conn = DBConnection(MONGODB_URI)
    db_conn.connect(DATABASE_NAME)
    
    # Get the database object
    db = db_conn.get_db()
    
    # Now you can use 'db' to interact with your database
    # For example, list the names of the collections in the database
    print("Collections:", db.list_collection_names())

    # Close the database connection when done
    db_conn.close()

if __name__ == "__main__":
    main()
