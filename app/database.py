from pymongo import MongoClient
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://mongo:27017")
client = MongoClient(MONGODB_URI)
db = client["foundlab"]
events = db["score_events"]
