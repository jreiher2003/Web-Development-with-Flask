from app import db
from app.models import AsciiArt

db.drop_all()
print "just dropped table"
db.create_all()


one = AsciiArt(title="another title", art="anoter art")
db.session.add(one)
db.session.commit()

print "Successful import"