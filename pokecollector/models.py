from pokecollector import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(1000))
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    