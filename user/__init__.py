# user/__init__.py

from flask import Blueprint
from flask_restful import Api
from user.views import DemoResource

# 1.创建蓝图对象
user_blu = Blueprint('user', __name__, url_prefix='/user')

# 2.创建蓝图对应的api对象
user_api = Api(user_blu)

# 3.添加类视图
user_api.add_resource(DemoResource, '/')