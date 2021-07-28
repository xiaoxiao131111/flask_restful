'''
通过method_decorators类属性 来设置类视图的装饰器
该属性接收两种类型数据
    列表形式： 所有请求方式都会使用列表中的装饰器
    字典形式： 给请求方式分别设置装饰器
'''
# 代码示例
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def deco1(f):

    def wrapper(*args, **kwargs):
        print('deco1')
        return f(*args, **kwargs)
    return wrapper


def deco2(f):
    def wrapper(*args, **kwargs):
        print('deco2')
        return f(*args, **kwargs)

    return wrapper

class DemoResource(Resource):
    # 通过metho_decorators类属性来设置类视图的装饰器
    # method_decorators = [deco1, deco2]  列表形式 所有请求方式都会使用
    method_decorators = {
        'get': [deco1],
        'post': [deco2]
    } # 字典形式 给请求方式分别设置装饰器

    def get(self):
        return {'foo': 'get'}

    def post(self):
        return {'foo': 'post'}

api.add_resource(DemoResource, '/')

if __name__ == '__main__':
    app.run(debug=True)