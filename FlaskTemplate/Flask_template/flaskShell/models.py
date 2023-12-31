from datetime import datetime
from flaskShell import db, loginManager
from flask_login import UserMixin


@loginManager.user_loader
def loadUser(user_id): 
	return User.query.get(int(user_id))


class User(db.Model, UserMixin): 
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
	password = db.Column(db.String(60), nullable=False)
	conversations = db.relationship("Conversation", backref="Name", lazy=True)

	def __repr__(self): 
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Conversation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

	def __repr__(self):
		return f"Conversation('{self.title}', '{self.date}')"
	
class Journal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)


	def __repr__(self):
		return f"Journal('{self.title}', '{self.date}', '{self.content})"

