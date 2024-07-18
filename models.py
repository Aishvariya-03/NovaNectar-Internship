from flask_login import UserMixin

# Example User model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.role = 'user'  # Default role

    def is_admin(self):
        return self.role == 'admin'
