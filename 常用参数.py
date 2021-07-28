'''
       常用参数
       default： 给参数设置默认值，如果不传递该参数会使用默认值-----str/int等
       required： 是否必须传递，默认False， 如果设置为True，不传递会返回400-----True/False
       location： 设置参数提取的位置-----字符串，args/form/json/files/headers/cookies
       type: 设置参数的转换类型（类型转换&格式校验）-----函数引用，int/内置类型/自定义函数
'''
from flask import Flask
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)

class DemoResource(Resource):
    def post(self):
        parser = RequestParser()

        parser.add_argument('name', required=True, location='json')
        parser.add_argument('age', default=10)

        args = parser.parse_args()

        print(args.name)
        print(args.age)

        return {'foo': 'post'}

api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)