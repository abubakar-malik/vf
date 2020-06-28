"""script to handle post request"""
import os
from datetime import datetime
from flask import Flask, json
from flaskext.mysql import MySQL
from dotenv import load_dotenv


load_dotenv()
mysql = MySQL()
application = Flask(__name__)

# MySQL Configuration
application.config['MYSQL_DATABASE_USER'] = os.environ["DB_USERNAME"]
application.config['MYSQL_DATABASE_PASSWORD'] = os.environ["DB_PASSWORD"]
application.config['MYSQL_DATABASE_DB'] = os.environ["DB_NAME"]
application.config['MYSQL_DATABASE_HOST'] = os.environ["DB_CONNECTIONSTRING"]
mysql.init_app(application)

@application.route('/', methods=['POST'])
def main():
    """main function"""
    return json.dumps({'message':'Hello from DateTime app!'}, sort_keys=True, indent=3)

# Insert "DateTime" into MySQL database
@application.route('/app', methods=['POST'])
def insert():
    """data insert function"""
    conn = None
    cursor = None
    try:
        datetime_now = datetime.now()
        current_time = datetime_now.strftime("%m-%d-%Y %H:%M:%S")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO datetime (value) VALUES (%s)", (datetime_now))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':"{\"Time saved\":\""+current_time+"\"}"},
                              sort_keys=True, indent=3)
        else:
            return json.dumps({'error':str(data[0])}, sort_keys=True, indent=3)
    except Exception as excep_msg:
        return json.dumps({'error':str(excep_msg)}, sort_keys=True, indent=3)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@application.route('/show', methods=['POST'])
def show():
    """data retrieve function"""
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM datetime")
        records = cursor.fetchall()

        records_dict = []
        for record in records:
            record_dict = {
                'DateTime': record[0]}
            records_dict.append(record_dict)

        return json.dumps(records_dict, sort_keys=True, indent=3)

    except Exception as excep_msg:
        print({'error':str(excep_msg)})
        return json.dumps({'error':str(excep_msg)}, sort_keys=True, indent=3)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=os.environ["PORT"])
