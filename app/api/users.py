from app.models.User import User
from flask import jsonify
from . import api


@api.route('/users/<int:id>')
def get_user(id):
  matches = User.objects(ID=id)
  if matches.count() > 0:
    user = matches.get(0)
    return jsonify(user.toJson())
  return "not found"

@api.route('/users')
def get_users():
  return jsonify \
  (
    {
      "users": [user.toJson() for user in User.objects()]
    }
  )
