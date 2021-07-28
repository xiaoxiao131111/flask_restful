# user/views.py

from flask_restful import Resource


class DemoResource(Resource):
    def get(self):
        return {'get': 'hello'}

    def post(self):
        return {'post': 'world'}