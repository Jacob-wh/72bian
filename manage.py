from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.common.database import db
from app import create_app
from constant import *
import os
from werkzeug.contrib.fixers import ProxyFix

app = create_app()
# 理解为管理app,为你的app添加额外命令去做不同的事情，如数据库映射，
# 绑定app
manager = Manager(app)
# 数据库映射把app和db句柄绑定
migrate = Migrate(app, db)
# 添加数据库映射的命令，从flask_migrate中引入
# 添加命令的一种方法，下方面有事一种方法，还有一种方法是继承Command类来添加，不同需求利用不同的方法，具体看官方文档
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    debug = os.environ.get('DEBUG', True)
    threaded = os.environ.get('THREADED', True)
    host = os.environ.get('HOST', APP_ADDR)
    port = int(os.environ.get('PORT', APP_PORT))
    app.run(debug=debug, host=host, port=port, threaded=threaded)


app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    manager.run()
