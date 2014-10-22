from flask import Blueprint

api = Blueprint('users', __name__)

from . import users
