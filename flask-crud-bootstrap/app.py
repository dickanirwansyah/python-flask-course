from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import logging as logger

flaskAppInstance = Flask(__name__)
flaskAppInstance.config['MYSQL_HOST'] = 'localhost'
flaskAppInstance.config['MYSQL_USER'] = 'root'
flaskAppInstance.config['MYSQL_PASSWORD'] = 'root'
flaskAppInstance.config['MYSQL_DB'] = 'dbpython'
mysql = MySQL(flaskAppInstance)

@flaskAppInstance.route('/')
def home():
    currentConnection = mysql.connection.cursor()
    currentConnection.execute("select * from computer")
    data = currentConnection.fetchall();
    currentConnection.close()
    return  render_template('home.html', computers = data)

@flaskAppInstance.route('/save', methods =["POST"])
def save():
    dataName = request.form['name']
    currentConnection = mysql.connection.cursor()
    currentConnection.execute("insert into computer(data) values ('"+dataName+"')")
    mysql.connection.commit()
    return redirect(url_for('home'))

@flaskAppInstance.route('/update', methods = ["POST"])
def update():
    dataId = request.form['id']
    dataName = request.form['name']
    currentConnection = mysql.connection.cursor()
    currentConnection.execute("update computer set data='"+dataName+"' where id='"+dataId+"'")
    mysql.connection.commit()
    return redirect(url_for('home'))

@flaskAppInstance.route('/destroy/<string:dataId>', methods = ["GET"])
def destroy(dataId):
    currentConnection = mysql.connection.cursor()
    currentConnection.execute("delete from computer where id='"+dataId+"'")
    mysql.connection.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    logger.debug("Starting the application")
    flaskAppInstance.run(host="0.0.0.0",port=5000, debug=True, use_reloader=True)