from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password):
        """
        Initialize MongoDB connection.
        """
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@{HOST}:{PORT}/"
            )
            self.database = self.client[DB]
            self.collection = self.database[COL]

        except PyMongoError as e:
            print(f"Connection failed: {e}")
            raise

    
    # CREATE
    
    def create(self, data):
        """
        Insert a document into the collection.

        :param data: Dictionary representing document
        :return: True if successful, else False
        """
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print(f"Insert failed: {e}")
                return False
        else:
            print("No data provided to insert.")
            return False

    
    # READ
    
    def read(self, query):
        """
        Retrieve documents from the collection.

        :param query: Dictionary query
        :return: List of matching documents
        """
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read failed: {e}")
            return []

    
    # UPDATE
    
    def update(self, query, new_values):
        """
        Update documents matching query.

        :param query: Dictionary query
        :param new_values: Dictionary of updated values
        :return: Number of documents modified
        """
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update failed: {e}")
            return 0

    
    # DELETE
    
    def delete(self, query):
        """
        Delete documents matching query.

        :param query: Dictionary query
        :return: Number of documents deleted
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete failed: {e}")
            return 0
