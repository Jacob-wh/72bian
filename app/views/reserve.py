from flask import Blueprint
from flask import render_template
reserve = Blueprint('reserve', __name__, url_prefix='/reserve')


@reserve.route('')
def home():
    return render_template('reserve.html')
