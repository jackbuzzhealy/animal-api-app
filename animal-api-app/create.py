from applications import db
from applications.models import Animals

db.drop_all()
db.create_all()

