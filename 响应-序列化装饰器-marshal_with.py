from flask import Flask
from flask_restful import Resource, Api, marshal_with, fields

app = Flask(__name__)
api = Api(app)

class User:
    def __init__(self):
        self.name = 'zs'
        self.age = 20,
        self.height = 1.8
        self.scores = [80, 90]
        self.info = {
            'gender': True
        }

fields = {
    'username': fields.String(attribute='name'),
    'age': fields.Integer(default=10),
    'height': fields.Float,
    'scores': fields.List(fields.Integer),
    'info': fields.Nested({'gender': fields.Boolean})
}

class DemoResource(Resource):
    method_decorators = {'post': [marshal_with(fields)]}
    def post(self):
        user1 = User()
        # 如果设置了marshal_with 装饰器， 可以直接返回模型对象
        return user1

api.add_resource(DemoResource, '/')

if __name__ == '__main__':
    app.run(debug=True)