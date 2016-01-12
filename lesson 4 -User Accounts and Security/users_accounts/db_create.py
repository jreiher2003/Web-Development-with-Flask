from app import db
# from app import models
from app.models import User

db.create_all() 


db.session.add(User("Jeff", "me@jeffreiher.com", "finn"))
db.session.add(User("Dodge", "me@donge.com", "dun"))

db.session.commit()
