from flask import Blueprint

reserve = Blueprint('reserve', __name__, url_prefix='/reserve')


@reserve.route('')
def home():
    return '主页'
