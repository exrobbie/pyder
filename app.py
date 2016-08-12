from flask import Flask, url_for, request, render_template, make_response
from apis import api_login
from werkzeug.utils import secure_filename

app = Flask(__name__)

api_login()


@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    print(request.cookies)
    resp.set_cookie('username', 'damowang')
    return resp


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name):
    print(request.method)
    return 'hello %s, the url is %s' % (name, url_for('hello', name=name))


@app.route('/guangzhou/')
def guangzhou_view():
    return render_template('guangzhou.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(render_template('404.html'), 404)


@app.errorhandler(401)
def no_permission(error):
    return make_response(render_template('401.html'),401)


if __name__ == '__main__':
    app.run()
