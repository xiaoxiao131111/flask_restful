from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)

class DemoResource(Resource):
    def get(self):
        # 1.创建请求解析器
        parser = RequestParser()
        # 2.添加参数规则

        parser.add_argument('name')
        parser.add_argument('age')

        # 3.执行解析  默认会从 查询字符串/post键值对 /post-json数据， 进行参数提取
        args = parser.parse_args()

        # 4. 获取参数
        print(args.name)
        print(args.age)

        return {'foo': 'get'}

api.add_resource(DemoResource, '/')

if __name__ == '__main__':
    app.run(debug=True)