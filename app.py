import pymysql
import secrets
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps
import penyedia 

def apikey_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        api_key = request.headers.get('api_key')

        if not api_key:
            return jsonify('key missing')

        cursor.execute('select * from apikey where apikeys = %s', api_key)

        if cursor.rowcount < 1:
            cursor.close()
            conn.close()
            return jsonify('invalid key')
        
        cursor.close()
        conn.close()
        return f(*args,**kwargs)
    return decorated

@app.route('/getkey')
def getapikey():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    api_key = secrets.token_urlsafe(64)
    cursor.execute("insert into apikey values (%s)", str(api_key))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(api_key)

@app.route('/costliving/read/<city_pick>/<country_pick>')
@apikey_required
def readSeletected(city_pick, country_pick):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("Select * from livingcost where City ='"+str(city_pick)+", "+str(country_pick)+"'")
        read_row = cursor.fetchall()
        response = jsonify(read_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/costliving')
@apikey_required
def welcome():
    return jsonify("welcome, sir.")

@app.route('/costliving/create', methods=['POST'])
def createRowData():
    try:
        _json = request.json
        kol1 = _json["city"]
        kol2 = _json["costoflivingindex"]
        kol3 = _json["rentindex"]
        kol4 = _json["costoflivingplusrent"]
        kol5 = _json["groceriesindex"]
        kol6 = _json["restopriceindex"]
        kol7 = _json["localpurchasingpowerindex"]

        if kol1 and kol2 and kol3 and kol4 and kol5 and kol6 and kol7 and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into livingcost values('"+str(kol1)+"',"+str(kol2)+","+str(kol3)+","+str(kol4)+","+str(kol6)+","+str(kol6)+","+str(kol7)+")"
            cursor.execute(query)
            conn.commit()
            response = jsonify('Data added!')
            response.status_code = 200
            return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/costliving/update/<city_pick>/<country_pick>', methods=['PUT'])
def updateSelected(city_pick, country_pick):
    try:
        _json = request.json
        kol1 = _json["city"]
        kol2 = _json["costoflivingindex"]
        kol3 = _json["rentindex"]
        kol4 = _json["costoflivingplusrent"]
        kol5 = _json["groceriesindex"]
        kol6 = _json["restopriceindex"]
        kol7 = _json["localpurchasingpowerindex"]

        values = ""


        if kol1 != "":
            values = values + "City = "+"'"+str(kol1)+"'"
        if kol2 != "":
            if len(values) == 0:
                values = values+"Cost_of_Living_Index = " + str(kol2)
            else:
                values = values+", Cost_of_Living_Index = " +str(kol2)
        if kol3 != "":
            if len(values) == 0:
                values = values+"Rent_Index = " + str(kol3)
            else:
                values = values +", Rent_Index = "+str(kol3)
        if kol4 != "":
            if len(values) == 0:
                values = values +"Cost_of_Living_Plus_Rent_Index = " + str(kol4)
            else:
                values = values +", Cost_of_Living_Plus_Rent_Index = "+str(kol4)
        if kol5 != "":
            if len(values) == 0:
                values = values+ "Groceries_Index = " + str(kol5)
            else:
                values = values +", Groceries_Index = "+str(kol5)
        if kol6 != "":
            if len(values) == 0:
                values = values +"Restaurant_Price_Index = "+ str(kol6)
            else:
                values = values +", Restaurant_Price_Index = "+str(kol6)
        if kol7 != "":
            if len(values) == 0:
                values = values +"Local_Purchasing_Power_Index = "+ str(kol7)
            else:
                values = values +", Local_Purchasing_Power_Index = "+str(kol7)

        query = "update livingcost set "+ values + " where City = '"+ str(city_pick)+", "+str(country_pick)+"'"

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        conn.commit()
        response = jsonify('Data Updated!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        


@app.route('/costliving/delete/<city_pick>/<country_pick>', methods=['DELETE'])
def deleteSelected(city_pick, country_pick):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("delete from livingcost where City = '"+str(city_pick)+", "+str(country_pick)+"'")
        conn.commit()
        response = jsonify('Data deleted!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    


if __name__ == "__main__":
    app.run()