from app import db
# from app import models
from app.models import User, BlogPost

db.create_all() 


# db.session.add(User("Jeff", "me@jeffreiher.com", "finn"))
# db.session.add(User("Dodge", "me@donge.com", "dun"))

db.session.add(BlogPost("Good", "I\'m good.",1))
db.session.add(BlogPost("Well", "I\'m well.",1))
db.session.add(BlogPost("Excellent", "I\'m excellent.",1))
db.session.add(BlogPost("Okay", "I\'m okay.",2))
db.session.add(BlogPost("postgres", "Local postres setup test.",2))

db.session.commit()
