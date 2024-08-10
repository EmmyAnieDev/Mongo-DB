import os

from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

password = os.environ.get('MONGO_DB_PWD')

mongo_db_url = f"mongodb+srv://SpiritCodes:{password}@tutorial.ffcuoii.mongodb.net/?retryWrites=true&w=majority&appName=Tutorial"
client = MongoClient(mongo_db_url)

# db = client.list_database_names()     # get the list of all databases in the cluster
# print(db)
#
# test_db = client.test
# collections = test_db.list_collection_names()      # get the list of all collections in the database
# #print(collections)


# initializing the database and collection
db = client.test
test_collection = db.testing


production_db = client.production               # automatically creating a database using code
person_collection = production_db.person_collection          # automatically creating a collection in the database