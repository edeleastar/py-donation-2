from app import createApp
from flask.ext.script import Manager

app = createApp()
manager = Manager(app)

if __name__ == '__main__':
  #app.run(debug=True)
  manager.run()