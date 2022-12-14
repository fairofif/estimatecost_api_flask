import pymysql
import secrets
from appflask import app
from config import mysql
from flask import jsonify, flash, request, make_response
from functools import wraps
from urllib.request import urlopen
import json
import requests
from thislogin import this_token_required, uClient, pClient, uDom2, pDom2

def getJsonLivingCostFromDomain2(city):
    url = 'http://'+uDom2+':'+pDom2+'@wakacipuy.my.id/region-recommendation/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/region-recommendation/get-living-cost/'+str(city)+'?token='+str(token)
    dataresponse = urlopen(url)
    _json = json.loads(dataresponse.read())
    return _json

def getJsonRentCostFromDomain2(city):
    url = 'http://'+uDom2+':'+pDom2+'@wakacipuy.my.id/region-recommendation/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/region-recommendation/get-rent-cost/'+str(city)+'?token='+str(token)
    dataresponse = urlopen(url)
    _json = json.loads(dataresponse.read())
    return _json

def getJsonGroceriesCostFromDomain2(city):
    url = 'http://'+uDom2+':'+pDom2+'@wakacipuy.my.id/region-recommendation/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/region-recommendation/get-groceries-cost/'+str(city)+'?token='+str(token)
    dataresponse = urlopen(url)
    _json = json.loads(dataresponse.read())
    return _json

def getJsonRestaurantCostFromDomain2(city):
    url = 'http://'+uDom2+':'+pDom2+'@wakacipuy.my.id/region-recommendation/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/region-recommendation/get-restaurant-cost/'+str(city)+'?token='+str(token)
    dataresponse = urlopen(url)
    _json = json.loads(dataresponse.read())
    return _json

def getJsonPowerCostFromDomain2(city):
    url = 'http://'+uDom2+':'+pDom2+'@wakacipuy.my.id/region-recommendation/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/region-recommendation/get-power-cost/'+str(city)+'?token='+str(token)
    dataresponse = urlopen(url)
    _json = json.loads(dataresponse.read())
    return _json

@app.route('/livingcost/<city>/<rolefirst>/<rolelast>/<exp>/<lifestyle>')
@this_token_required
def getLivingCost(city,rolefirst,rolelast,exp,lifestyle):
    livcostmid = getJsonLivingCostFromDomain2(city)['living_cost_in_usd']*12
    rentcostmid = getJsonRentCostFromDomain2(city)['rent_cost_in_usd']*12
    livcostmid = livcostmid + rentcostmid
    url = 'http://'+uClient+':'+pClient+'@wakacipuy.my.id/estimatecost/login'
    response = requests.get(url)
    response = (response.json())    
    token = response['token']

    url = 'https://wakacipuy.my.id/estimatecost/getsalaries/'+str(city)+'/'+str(rolefirst)+'/'+str(rolelast)+'/'+str(exp)+'/f?token='+str(token)
    dataresponse = urlopen(url)
    jsonsalary = json.loads(dataresponse.read())
    
    minsalary = jsonsalary['min_salary_usd']/1
    maxsalary = jsonsalary['max_salary_usd']/1
    avgsalary = jsonsalary['avg_salary_usd']/1
    print(minsalary,maxsalary,avgsalary)

    livcosthigh = livcostmid*3
    livcostlow = livcostmid - (livcostmid * 0.3)
    
    minspendlow = minsalary - livcostlow
    maxspendlow = maxsalary - livcostlow
    avgspendlow = avgsalary - livcostlow

    minspendmid = minsalary - livcostmid
    maxspendmid = maxsalary - livcostmid
    avgspendmid = avgsalary - livcostmid

    minspendhigh = minsalary - livcosthigh
    maxspendhigh = maxsalary - livcosthigh
    avgspendhigh = avgsalary - livcosthigh

    _json = {}


    if str(lifestyle) == "high":
        _json['annual_living_cost_in_USD_with_high_lifestyle'] = livcosthigh
        _json['annual_minimum_salary_in_USD'] = minsalary
        _json['annual_average_salary_in_USD'] = avgsalary
        _json['annual_maximum_salary_in_USD'] = maxsalary
        _json['annual_spent_money_if_minimum_salary_with_high_lifestyle'] = minspendhigh
        _json['annual_spent_money_if_average_salary_with_high_lifestyle'] = avgspendhigh
        _json['annual_spent_money_if_maximum_salary_with_high_lifestyle'] = maxspendhigh
    elif str(lifestyle) == "mid":
        _json['annual_living_cost_in_USD_with_mid_lifestyle'] = livcostmid
        _json['annual_minimum_salary_in_USD'] = minsalary
        _json['annual_average_salary_in_USD'] = avgsalary
        _json['annual_maximum_salary_in_USD'] = maxsalary
        _json['annual_spent_money_if_minimum_salary_with_mid_lifestyle'] = minspendmid
        _json['annual_spent_money_if_average_salary_with_mid_lifestyle'] = avgspendmid
        _json['annual_spent_money_if_maximum_salary_with_mid_lifestyle'] = maxspendmid
    elif str(lifestyle) == "low":
        _json['annual_living_cost_in_USD_with_low_lifestyle'] = livcostlow
        _json['annual_minimum_salary_in_USD'] = minsalary
        _json['annual_average_salary_in_USD'] = avgsalary
        _json['annual_maximum_salary_in_USD'] = maxsalary
        _json['annual_spent_money_if_minimum_salary_with_low_lifestyle'] = minspendlow
        _json['annual_spent_money_if_average_salary_with_low_lifestyle'] = avgspendlow
        _json['annual_spent_money_if_maximum_salary_with_low_lifestyle'] = maxspendlow
    elif str(lifestyle) == "all":
        _json['annual_living_cost_in_USD_with_low_lifestyle'] = livcostlow
        _json['annual_living_cost_in_USD_with_mid_lifestyle'] = livcostmid
        _json['annual_living_cost_in_USD_with_high_lifestyle'] = livcosthigh
        _json['annual_minimum_salary_in_USD'] = minsalary
        _json['annual_average_salary_in_USD'] = avgsalary
        _json['annual_maximum_salary_in_USD'] = maxsalary
        _json['annual_spent_money_if_minimum_salary_with_low_lifestyle'] = minspendlow
        _json['annual_spent_money_if_average_salary_with_low_lifestyle'] = avgspendlow
        _json['annual_spent_money_if_maximum_salary_with_low_lifestyle'] = maxspendlow
        _json['annual_spent_money_if_minimum_salary_with_mid_lifestyle'] = minspendmid
        _json['annual_spent_money_if_average_salary_with_mid_lifestyle'] = avgspendmid
        _json['annual_spent_money_if_maximum_salary_with_mid_lifestyle'] = maxspendmid
        _json['annual_spent_money_if_minimum_salary_with_high_lifestyle'] = minspendhigh
        _json['annual_spent_money_if_average_salary_with_high_lifestyle'] = avgspendhigh
        _json['annual_spent_money_if_maximum_salary_with_high_lifestyle'] = maxspendhigh
    _json = json.dumps(_json)

    return _json

@app.route('/allavgcost/<city>/<yearormonth>')
def allAverage(city, yearormonth):
    rentcost = getJsonRentCostFromDomain2(city)['rent_cost_in_usd']
    groceriescost = getJsonGroceriesCostFromDomain2(city)['groceries_cost_in_usd']
    restaurantcost = getJsonRestaurantCostFromDomain2(city)['restaurant_cost_in_usd']
    localpowerpurchasecost = getJsonPowerCostFromDomain2(city)['local_purchasing_power_cost_in_usd']
    _json = {}
    if yearormonth == "year":
        rentcost *= 12
        groceriescost *= 12
        restaurantcost *= 12
        localpowerpurchasecost *= 12
        _json["Monthly_or_Yearly"] = "yearly (annual)"
    else:
        _json['Monthly_or_Yearly'] = "monthly"

    
    _json["rent_cost_in_usd"] = rentcost
    _json["groceries_cost_in_usd"] = groceriescost
    _json["restaurant_cost_in_usd"] = restaurantcost
    _json["local_purchasing_power_cost_in_usd"] = localpowerpurchasecost
    _json = json.dumps(_json)

    return _json