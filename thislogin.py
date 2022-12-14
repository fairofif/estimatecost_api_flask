import pymysql
import secrets
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps
import jwt
import datetime

app.config['SECRET_KEY'] = "wakacipuyitubukanwakadingdong"
uClient = 'clientkafi'
pClient = 'clientkafi'
uDom2 = 'clientrofif'
pDom2 = 'clientrofif'
def this_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is Missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        except:
            return jsonify({'message': 'Token is Invalid'}), 403

        return f(*args, **kwargs)
    return decorated
    

@app.route('/thislogin')
def thislogin():
    auth = request.authorization
    if auth and isThisLoginValid(auth.username, auth.password) == True:
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.encode().decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

def isThisLoginValid(username, password):
    status = False
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from account_this where username = '"+username+"' and password = '"+password+"'")
    if cursor.rowcount > 0:
        return True
    cursor.close()
    conn.close()
    return status

