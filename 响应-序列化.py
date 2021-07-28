'''
flask-restful通过marshal函数，来完成序列化处理
操作步骤如下：
    定义序列化规则：序列化规则={字段名：序列化类型}
    marshal函数： 按照序列化规则，将模型对象转为字典： 序列化后的字典=marshal(模型对象， 序列化规则)
'''
"""
常用序列化类型
    String： 可转换 字符串类型属性
    Integer： 可转换 整数类型属性
    Float： 可转换 浮点数类型属性
    List： 可转换 列表类型属性， 要求列表中元素类型唯一
    Nested： 可转换 字典类型属性
"""
# 代码示例
from flask import Flask
from flask_restful import Api, marshal, fields, Resource


app = Flask(__name__)
api = Api(app)

class User():
    def __init__(self):
        self.name = 'zs'
        self.age = 20
        self.height = 1.8
        self.score = [80, 90]
        self.info = {
            'gender': True
        }

# 序列化规则
fields = {
    'username': fields.String(attribute='name'),  # 指定对应的模型属性
    'age': fields.Integer(default=10),  # 设置默认值
    'height': fields.Float,
    'score': fields.List(fields.Integer),  # 元素类型唯一
    'info': fields.Nested({'gender': fields.Boolean})
}


class DemoResource(Resource):
    def get(self):
        user1 = User()

        # marshal函数可以按照指定的序列化规则将 模型对象 转为字典
        return marshal(user1, fields, envelope='data')

api.add_resource(DemoResource, '/')

if __name__ == '__main__':
    app.run(debug=True)