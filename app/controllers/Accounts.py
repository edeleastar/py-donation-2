from flask import render_template
from . import accounts


@accounts.route('/')
def index():
  return render_template('accounts/index.html')
