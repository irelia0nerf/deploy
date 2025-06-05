from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://mongo:27017")
client = AsyncIOMotorClient(MONGODB_URI)
db = client["foundlab"]
events = db["score_events"]
