import os, json, mysql.connector
from mysql.connector import errorcode
import settings


def mysqlCallback():
    print('Connected')

try :
    connection = mysql.connector.connect(
        user = os.getenv("SQL_USER"),
        password = os.getenv("SQL_PWD"),
        host = os.getenv("SQL_HOST"),
        database = os.getenv("SQL_DB")
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    mysqlCallback()
    cursor = connection.cursor()
    queryTerm = "'freon'"
    query = """SELECT * FROM Dictionary WHERE Expression={queryTerm}""".format(queryTerm=queryTerm)
    try: 
        data = cursor.execute(query)
        for row in cursor:
            print(json.dumps(row, indent=2))
    except mysql.connector.Error as err:
        print(err)
    connection.close()


