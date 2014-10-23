from app import db

class User(db.DynamicDocument):
  firstname = db.StringField()
  lastname =  db.StringField()
  email = db.StringField()
  password = db.StringField()
  ID = db.IntField(min_value=1)

  def toJson(self):
    json_user = \
    {
      'ID'        : self.ID,
      'firstname' : self.firstname,
      'lastname'  : self.lastname,
      'email'     : self.email,
      'password'  : self.password
    }
    return json_user
