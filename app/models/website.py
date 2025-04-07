from app import mongo
from bson import ObjectId
from datetime import datetime
from flask import render_template, Blueprint

def create_website(user_id, business_type, industry, content, layout):
    website = {
        "user_id": str(user_id),
        "business_type": business_type,
        "industry": industry,
        "content": content,
        "layout": layout,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    return mongo.db.websites.insert_one(website)

def get_websites_by_user(user_id):
    return list(mongo.db.websites.find({"user_id": str(user_id)}))

def get_website_by_id(website_id):
    return mongo.db.websites.find_one({"_id": ObjectId(website_id)})

def update_website(website_id, update_data):
    update_data["updated_at"] = datetime.utcnow()
    return mongo.db.websites.update_one({"_id": ObjectId(website_id)}, {"$set": update_data})

def delete_website(website_id):
    return mongo.db.websites.delete_one({"_id": ObjectId(website_id)})