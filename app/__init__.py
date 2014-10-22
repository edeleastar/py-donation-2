from flask import Flask

SECRET_KEY = 'development key'

def createApp():
  app = Flask(__name__)
  app.config.from_object(__name__)

  from .controllers import accounts as account_blueprint
  app.register_blueprint(account_blueprint)

  from .controllers import donate as donate_blueprint
  app.register_blueprint(donate_blueprint)

  from .api import api as api_blueprint
  app.register_blueprint(api_blueprint)


  return app
