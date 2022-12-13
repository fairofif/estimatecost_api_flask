from appflask import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'wakacipu_rofif'
app.config['MYSQL_DATABASE_PASSWORD'] = '7601labtek5'
app.config['MYSQL_DATABASE_DB'] = 'wakacipu_ITSalaries'
app.config['MYSQL_DATABASE_HOST'] = '103.163.138.244'
mysql.init_app(app)