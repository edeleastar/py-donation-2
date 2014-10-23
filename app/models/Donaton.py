from app import db

class Donation(db.DynamicDocument):
  amount = db.StringField()
  method =  db.StringField()
  ID = db.IntField(min_value=1)
