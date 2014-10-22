from app.models.User import User, users
from flask import jsonify
from . import api

@api.route('/users/<int:id>')
def get_user(id):
  user = User.findById(id)
  if user != None:
    return jsonify(user.toJson())
  else:
    return "not found"

@api.route('/users')
def get_users():
  return jsonify \
  (
    {
      "users": [user.toJson() for user in users.values()]
    }
  )
