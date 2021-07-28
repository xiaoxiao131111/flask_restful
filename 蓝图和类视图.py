# main.py

from flask import Flask
from user import user_blu

app = Flask(__name__)
# 4.注册蓝图
app.register_blueprint(user_blu)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, port=8000)