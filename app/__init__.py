from flask import Flask
from flask.ext.mongoengine import MongoEngine

SECRET_KEY = 'development key'
MONGODB_SETTINGS =  {"DB": "py_donation"}

db = MongoEngine()

def createApp():
  app = Flask(__name__)
  app.config.from_object(__name__)

  db.init_app(app)

  from .controllers import accounts as account_blueprint
  app.register_blueprint(account_blueprint)

  from .controllers import donate as donate_blueprint
  app.register_blueprint(donate_blueprint)

  from .api import api as api_blueprint
  app.register_blueprint(api_blueprint)


  return app
