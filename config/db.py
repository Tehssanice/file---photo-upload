from pymongo import MongoClient
from config.settings import Settings

settings = Settings()

MongoClient = MongoClient(settings.mongo_url)
db = MongoClient.UserData
