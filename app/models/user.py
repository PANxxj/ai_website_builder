from app.extension import mongo
from datetime import datetime
from bson.objectid import ObjectId
from flask import render_template, Blueprint

def create_user(email, hashed_password):
    user = {"email": email, "password": hashed_password, "created_at": datetime.utcnow()}
    return mongo.db.users.insert_one(user)

def find_user_by_email(email):
    return mongo.db.users.find_one({"email": email})

def find_user_by_id(user_id):
    return mongo.db.users.find_one({"_id": ObjectId(user_id)})
