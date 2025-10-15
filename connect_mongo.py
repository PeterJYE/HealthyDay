from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

# Read variables from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

print("✅ Connected successfully to:", DB_NAME)
