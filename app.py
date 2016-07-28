from flask import Flask, url_for, request, render_template, make_response, redirect, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)


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


@app.route('/api/user/login', methods=['POST', 'GET'])
def api_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        valid = valid_login(username, password)
    elif request.method == 'GET':
        username = request.args['username']
        password = request.args.get('password', '')
        valid = valid_login(username, password='haizhi123')
    if valid == 1:
        return redirect(url_for('index'))
    else:
        abort(411)


def valid_login(username, password):
    if username == 'litianao' and password == 'haizhi123':
        return 1
    else:
        return 0


@app.errorhandler(404)
def not_found(error):
    return make_response(render_template('404.html'),404)

if __name__ == '__main__':
    app.run()
