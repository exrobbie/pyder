from flask import Flask, request, redirect, abort, url_for

app = Flask(__name__)


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