import pymysql
import secrets
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps
import penyedia 
from urllib.request import urlopen
import json
import requests

# contoh pemanggilan domain 1 buat di domain 2, tinggal variasi mainin di variable2nya
@app.route('/cobaaja')
def cobaaja():

    url = 'http://clientkafi:clientkafi@wakacipuy.my.id/estimatecost/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/estimatecost/getsalaries/Munich/Software/f/f/Senior?token='+str(token)
    dataresponse = urlopen(url)
    _json = json.loads(dataresponse.read())
    
    return _json


if __name__ == "__main__":
    app.run()