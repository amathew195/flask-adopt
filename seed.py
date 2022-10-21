from models import db, Pet
from app import app

db.drop_all()
db.create_all()


fluffy = Pet(
    name="fluffy",
    species="cat",
    photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg',
    age="baby",
    notes='loves milk',
    available=True
)

grumpy = Pet(
    name="grumpy",
    species="dog",
    photo_url='https://static.boredpanda.com/blog/wp-content/uploads/2015/07/grumpy-dog-earl-puggle-meme-18.jpg',
    age="adult",
    notes='loves playing fetch',
    available=False
)

db.session.add_all([grumpy, fluffy])


db.session.commit()
