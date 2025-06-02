import os

DATABASE_URI = "postgresql://username:password@your-cloud-sql-ip/dbname"

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
