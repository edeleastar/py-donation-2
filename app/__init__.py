from flask import Flask

def createApp():
  app = Flask(__name__)

  from .controllers import accounts as account_blueprint
  app.register_blueprint(account_blueprint)

  return app
