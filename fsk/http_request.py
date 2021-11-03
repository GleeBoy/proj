from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    from utils import cheese  # 下面附上utils模块的实现
    cheese()
    return 'Yet another hello!'


if __name__ == '__main__':
    app.run()

