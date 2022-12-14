import pymysql
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps
from clientlogin import token_required


# kalo parameter route gadipake isi aja sama f
# misal wakacipuy.my.id/estimatecost/getsalaries/Munich/Software/f/f/Senior
@app.route('/getsalaries/<city>/<rolefirst>/<rolelast>/<exp>/<seniorlvl>')
@token_required
def getsalary(city,rolefirst,rolelast,exp,seniorlvl):
    arrParameter = []
    arrPositionParameter = []
    if str(city) != 'f':
        arrParameter += [str(city)]
        arrPositionParameter += [1]
    if str(rolefirst) != 'f':
        if str(rolelast) != 'f':
            arrParameter += [str(str(rolefirst)+" "+str(rolelast))]
            arrPositionParameter += [3]
        else:
            arrParameter += [str(rolefirst)]
            arrPositionParameter += [2]
    if str(exp) != 'f':
        arrParameter += [str(exp)]
        arrPositionParameter += [4]
    if str(seniorlvl) != 'f':
        arrParameter += [str(seniorlvl)]
        arrPositionParameter += [5]

    queryselect = 'select (min(salary)*1.07) as min_salary_usd, (max(salary)*1.07) as max_salary_usd, (avg(salary)*1.07) as avg_salary_usd FROM ( (SELECT City, (this_year_brutto+this_year_bonus) as salary FROM salariesIT WHERE'
    queryclose = ') as t1 )'
    querycondition = ""
    for i in range(len(arrParameter)):
        if arrPositionParameter[i] == 1:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " City = '" + arrParameter[i] + "' "
        if arrPositionParameter[i] == 2:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + "  Position like '" + arrParameter[i] + "%' "
        if arrPositionParameter[i] == 3:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " Position = '" + arrParameter[i] + "' "
        if arrPositionParameter[i] == 4:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " years_experience = '" + arrParameter[i] + "' "
        if arrPositionParameter[i] == 5:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " level = '" + arrParameter[i] + "' "
    
    queryfinal = queryselect + querycondition + queryclose
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(queryfinal)
        read_row = cursor.fetchone()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify(e)
    finally:
        cursor.close()
        conn.close()


# kalo parameter route gadipake isi aja sama f
# misal wakacipuy.my.id/estimatecost/getsalaries/Munich/Software/f/f/Senior
@app.route('/getvacationdays/<city>/<rolefirst>/<rolelast>/<exp>/<seniorlvl>')
@token_required
def getvacationdays(city,rolefirst,rolelast,exp,seniorlvl):
    arrParameter = []
    arrPositionParameter = []
    if str(city) != 'f':
        arrParameter += [str(city)]
        arrPositionParameter += [1]
    if str(rolefirst) != 'f':
        if str(rolelast) != 'f':
            arrParameter += [str(str(rolefirst)+" "+str(rolelast))]
            arrPositionParameter += [3]
        else:
            arrParameter += [str(rolefirst)]
            arrPositionParameter += [2]
    if str(exp) != 'f':
        arrParameter += [str(exp)]
        arrPositionParameter += [4]
    if str(seniorlvl) != 'f':
        arrParameter += [str(seniorlvl)]
        arrPositionParameter += [5]

    queryselect = 'select min(vacation_days) as min_vacation_days, max(vacation_days) as max_vacation_days, avg(vacation_days) as avg_vacation_days FROM ( (SELECT City, vacation_days FROM salariesIT WHERE'
    queryclose = ') as t1 )'
    querycondition = ""
    for i in range(len(arrParameter)):
        if arrPositionParameter[i] == 1:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " City = '" + arrParameter[i] + "' "
        if arrPositionParameter[i] == 2:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + "  Position like '" + arrParameter[i] + "%' "
        if arrPositionParameter[i] == 3:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " Position = '" + arrParameter[i] + "' "
        if arrPositionParameter[i] == 4:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " years_experience = '" + arrParameter[i] + "' "
        if arrPositionParameter[i] == 5:
            if i != 0:
                querycondition = querycondition + " and "
            querycondition = querycondition + " level = '" + arrParameter[i] + "' "
    
    queryfinal = queryselect + querycondition + queryclose
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(queryfinal)
        read_row = cursor.fetchone()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify(e)
    finally:
        cursor.close()
        conn.close()
