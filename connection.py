from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv() 
client = MongoClient(os.getenv("MONGODB_URI"), tlsCAFile=certifi.where())

for db_name in client.list_database_names():
    print(db_name)

client.close()