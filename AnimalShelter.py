from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:46601/test?authSource=AAC' % ("aacuser", "thepassword"))
        self.database = self.client['AAC']
        
    # Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    # Method to implement the R in CRUD
    def read(self, criteria = None):
        # when criteria is not none then return all rows that match
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id": False})
        
        # when no criteria then all rows are returned
        else:
            data = self.database.animals.find({}, {"_id": False})
        
        return list(data)
    
    # Method to implement the U in CRUD
    def update(self, criteria, data):
        if criteria is not None and data is not None:
            result = self.database.animals.update_many(criteria, {"$set": data})
            return result.modified_count
        else:
            raise Exception("Nothing to update.")
           
    # Method to implement the D in CRUD
    def delete(self, criteria = None):
        if criteria is not None:
            result = self.database.animals.delete_many(criteria)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete.")
            