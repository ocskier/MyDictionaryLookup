import mysql.connector

from mysql.connector import errorcode
from db.connection import connection

cursor = connection.cursor()

def find(queryTerm):
    stringQuery = """'{input}'""".format(input=queryTerm)
    searchQuery = """SELECT * FROM Dictionary WHERE Expression={query}""".format(query=stringQuery)
    print(searchQuery)
    try: 
        cursor.execute(searchQuery)
        rows=cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        return err

def create(exp,definition):
    addQuery = """INSERT INTO Dictionary(Expression,Definition) VALUES ('{exp}','{definition}')""".format(exp=exp,definition=definition)
    print(addQuery)
    try: 
        cursor.execute(addQuery)
        connection.commit()
        id = cursor.lastrowid
        return id
    except mysql.connector.Error as err:
        return err

def end():
    cursor.close()