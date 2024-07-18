from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# Example User model (from models.py)
from app.models import User

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Replace with your logic to load user from database or storage
    return User(user_id)  # Example: assuming User model exists in models.py

# Import routes after app and login_manager are created
from app import routes
