from pokecollector import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(1000))
    cards = db.relationship('UserCards', backref='user', cascade='all, delete-orphan', lazy=True)
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    
class UserCards(db.Model):    
    __tablename__ = 'user_cards'     

    user_cards_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.String(50), nullable=True)
    card_name = db.Column(db.String(50), nullable=True)
    card_number = db.Column(db.Integer, nullable=True)
    card_image = db.Column(db.String(100), nullable=True)
    set_id = db.Column(db.String(50), nullable=True)

    