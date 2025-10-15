# food.py
from connect_mongo import db
from bson import ObjectId
from datetime import datetime

class Food:
    def __init__(self, name, category, calories, protein, carbs, fat, user_id=None, expiry_date=None):
        self.user_id = user_id
        self.name = name
        self.category = category
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.expiry_date = expiry_date
        self.created_at = datetime.utcnow()

    def to_dict(self):
        """Convert class instance to dictionary for MongoDB"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "category": self.category,
            "calories": self.calories,
            "protein": self.protein,
            "carbs": self.carbs,
            "fat": self.fat,
            "expiry_date": self.expiry_date,
            "created_at": self.created_at
        }

    def save(self):
        """Insert this food into MongoDB"""
        foods = db["foods"]
        result = foods.insert_one(self.to_dict())
        print(f"✅ Food '{self.name}' saved with _id: {result.inserted_id}")
        return result.inserted_id

    @staticmethod
    def find_by_user(user_id):
        """Find all foods that belong to a given user"""
        foods = db["foods"]
        return list(foods.find({"user_id": user_id}))

    @staticmethod
    def find_one(food_id):
        """Find one food by its ObjectId"""
        foods = db["foods"]
        return foods.find_one({"_id": ObjectId(food_id)})

    @staticmethod
    def delete(food_id):
        """Delete one food by its ObjectId"""
        foods = db["foods"]
        result = foods.delete_one({"_id": ObjectId(food_id)})
        print(f"🗑️ Deleted {result.deleted_count} food(s)")
