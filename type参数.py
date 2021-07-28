from flask import Flask
from flask_restful.reqparse import RequestParser
from flask_restful import Api, Resource
from flask_restful.inputs import *

app = Flask(__name__)
api = Api(app)

# 自定义函数进行参数校验和转换
def func1(value): # 必须定义形参来接收传递来的参数
    if re.match(r'^user', value):
        return value[5:]  # 转换完，还需要将结果返回
    else:
        raise ValueError('age参数格式错误')  # 校验失败， 会将错误信息以json形式返回


class DemoResource(Resource):
    def put(self):
        parser = RequestParser()

        parser.add_argument('name')
        # parser.add_argument('age', type=int)  # 转为int类型

        # parser.add_argument('age', type=boolean)  # 转为bool类型   1/0 true/false
        # parser.add_argument('age', type=date)  # 日期 转为datetime类型   YYYY-mm-dd
        # parser.add_argument('age', type=datetime_from_iso8601)  # 时间 转为datetime类型  2012-01-01T23:30:00+02:00
        # parser.add_argument('age', type=int_range(5, 10))  # 转为int类型 限定范围[5, 10]

        # parser.add_argument('age', type=regex(r'^1[3-9]\d{9}$'))  # 要求匹配正则
        parser.add_argument('age', type=func1)  # 自定义函数

        args = parser.parse_args()

        print(args.name)
        print(args.age)
        print(type(args.age))

        return {'foo': 'put'}

api.add_resource(DemoResource, '/')

if __name__ == '__main__':
    app.run(debug=True)