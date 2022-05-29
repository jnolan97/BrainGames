import sqlite3
import json
import os
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, send_file, redirect, url_for, Blueprint, Response
# from connection.sqlite3_connection import Sqlite3Connection, sqlite3_call
from flask_mysqldb import MySQL

app = Flask(__name__)
# db = SQLAlchemy(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'schedulerv1'
 
mysql = MySQL(app)

@app.route("/")
def main():
    # username = 'dummyadmin'
    # password = 'admin1234'
    # email = 'dummy@word.net'
    # phone = '1234456677'
    # #Creating a connection cursor
    cursor = mysql.connection.cursor()
    # #Executing SQL Statements
    select_query = cursor.execute('''select * from users ''')
    # # cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
    # user_id = cursor.execute('''select id from users ORDER BY id DESC LIMIT 1''')
    # cursor.execute(''' INSERT INTO users VALUES(%s,NULL,%s,%s,%s,%s)''',((user_id+1),username,password,email,phone))
    # # cursor.execute(''' DELETE FROM table_name WHERE condition ''')
    
    #Saving the Actions performed on the DB
    mysql.connection.commit()
    print(select_query)
    #Closing the cursor
    cursor.close()
    return Response('''results:{select_query}'''.format(select_query=select_query), 200)

if __name__ == "__main__":
    # Only for debugging while developing and running main.py (without docker):
    # -> choose a port higher than 1000 to avoid permission problems
    #app.run(host="0.0.0.0", port=5000, debug=True)
    # Port 80 configuration to run via docker-compose up
    app.run(host="0.0.0.0", port=5000, debug=True)