# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def get_user(user_id):
        return User.query.filter_by(id=user_id).first()

    def update_user(user_id, name, email):
        user = User.query.filter_by(id=user_id).first()
        user.name = name
        user.email = email
        db.session.commit()