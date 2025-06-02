import logging
from flask import Flask
from models import db
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def setup_database():
    """Initialize the database and handle potential errors."""
    try:
        with app.app_context():
            db.create_all()
            logging.info("✅ Database initialized successfully!")
    except Exception as e:
        logging.error(f"❌ Database setup failed: {e}")

if __name__ == "__main__":
    setup_database()