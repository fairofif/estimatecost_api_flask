import pymysql
import secrets
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps

@app.route('/getminsalary/<citypick>')
def getMinSalaryFromCity(citypick):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select min(salary) as min_salary FROM ( (SELECT city, (this_year_brutto+this_year_bonus) as salary FROM salariesIT WHERE city = '"+str(citypick)+"') as t1 )")
        read_row = cursor.fetchall()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/getmaxsalary/<citypick>')
def getMinSalaryFromCity(citypick):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select max(salary) as max_salary FROM ( (SELECT city, (this_year_brutto+this_year_bonus) as salary FROM salariesIT WHERE city = '"+str(citypick)+"') as t1 )")
        read_row = cursor.fetchall()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/getavgsalary/<citypick>')
def getMinSalaryFromCity(citypick):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select avg(salary) as avg_salary FROM ( (SELECT city, (this_year_brutto+this_year_bonus) as salary FROM salariesIT WHERE city = '"+str(citypick)+"') as t1 )")
        read_row = cursor.fetchall()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/getminsalary/<citypick>/<rolepickfirst>/<rolepicklast>')
def getMinSalaryFromCityWithRole(citypick,rolepickfirst,rolepicklast):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if str(rolepicklast) == ".":
            query = "select min(salary) as min_salary FROM ( (SELECT city, (this_year_brutto+this_year_bonus) as salary FROM salariesIT WHERE city = '"+str(citypick)+"' and Position like '"+str(rolepickfirst)+"%') as t1 )"
        else:
            query = "select min(salary) as min_salary FROM ( (SELECT city, (this_year_brutto+this_year_bonus) as salary FROM salariesIT WHERE city = '"+str(citypick)+"' and Position = '"+str(rolepickfirst)+" "+str(rolepicklast)+"') as t1 )"
        cursor.execute(query)
        read_row = cursor.fetchall()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

