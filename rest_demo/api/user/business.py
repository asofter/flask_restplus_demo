from rest_demo import db
from rest_demo.database.models import User


def create_user(data):
    user = User(
        email=data.get('email'),
        password=data.get('password')
    )
    # insert the user
    db.session.add(user)
    db.session.commit()

    return user


def update_user(user, data):
    email = data.get('email', None)
    if email:
        user.email = email

    password = data.get('password', None)
    if password:
        user.password = password

    db.session.add(user)
    db.session.commit()