import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/find-computer-byid/<string:computerId>', methods=['GET'])
def find_computer_byid(computerId):
    try:
        con = mysql.connect()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "select id as codeId, data as nameComputer from computer where id='"+computerId+"'"
        cursor.execute(sqlQuery)
        row = cursor.fetchone()
        if row:
            message = {
                'status': 200,
                'message': 'data found !',
                'data': row
            }
            response = jsonify(message)
            response.status_code = 200
            return response
        else:
            message = {
                'status': 404,
                'message': 'sorry data is not found !',
            }
            response = jsonify(message)
            response.status_code = 404
            return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/save-computer', methods=['POST'])
def save_computer():
    try:
        _json = request.json
        _data = _json['data']
        con = mysql.connect()
        cursor = con.cursor()
        sqlQueryInsert = "insert into computer(data) values(%s)"
        bindDataInsert = (_data)
        if _data and request.method == 'POST':

            cursor.execute("select * from computer where data='"+_data+"'")
            row = cursor.fetchone()
            if row:
                message = {
                    'status' : 409,
                    'message' : 'sorry data is already taken'
                }
                response = jsonify(message)
                response.status_code = 409
                return response
            else:
                cursor.execute(sqlQueryInsert, bindDataInsert)
                con.commit()
                respose = jsonify('data computer added successfully')
                respose.status_code = 200
                return respose
        else:
            return not_found
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

@app.route('/computers', methods=['GET'])
def list_computers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select id, data from computer")
        computersRows = cursor.fetchall()
        response = jsonify(computersRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error = None):
    message = {
        'status' : 404,
        'message' : 'Record not found '+request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run()