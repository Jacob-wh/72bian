from .common.database import init_db
from flask import Flask
from config import Config


def create_app():
    # 初始化app
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    # 数据库与app绑定
    init_db(app)

    return app
