import pymysql
import secrets
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps
import penyedia, pemanfaat
from urllib.request import urlopen
import json
import requests


if __name__ == "__main__":
    app.run()