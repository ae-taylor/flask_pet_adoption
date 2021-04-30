from models import Pet, db, Post
from app import app
# Create all tables
db.drop_all()
db.create_all()
# If table isn't empty, empty it
Pet.query.delete()
# Add user
anna = Pet(name='Anna', species='Taylor', photo_url="https://media.istockphoto.com/photos/cool-guy-in-sunglasses-picture-id153749383",
age='young', available=True)
# Add new objects to session, so they'll persist
db.session.add(anna)
# Commit--otherwise, this never gets saved!
db.session.commit()

#run app.y and seed.py to see if this works
