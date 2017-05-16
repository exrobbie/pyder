from flask import Flask, render_template, make_response, request, redirect, abort, url_for
from spider import get_magnet
print(get_magnet)
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


@app.route('/guangzhou/')
def guangzhou_view():
    return render_template('guangzhou.html')


@app.route('/magnet', methods=['GET'])
def magnet_page():
    return render_template('magnet.html')


@app.route('/magnet', methods=['POST'])
def magnet_data():
    get_magnet()
    return make_response("{'name': 'robbie'}", 200)


@app.route('/api/user/login', methods=['POST', 'GET'])
def api_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    elif request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
    if valid_login(username, password):
        return redirect(url_for('index'))
    else:
        return abort(401)


def valid_login(username, password):
    if username == 'litianao' and password == 'haizhi123':
        return 1
    else:
        return 0


@app.errorhandler(404)
def not_found(error):
    return make_response(render_template('404.html'), 404)


@app.errorhandler(401)
def no_permission(error):
    return make_response(render_template('401.html'), 401)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
