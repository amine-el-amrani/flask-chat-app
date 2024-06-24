import os
from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(f'{MONGODB_URI}')

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})