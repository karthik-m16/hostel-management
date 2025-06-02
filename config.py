import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # If DATABASE_URI is not defined, use a local SQLite database as fallback.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or "sqlite:///db.sqlite3"  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY") or "default_secret_key"
