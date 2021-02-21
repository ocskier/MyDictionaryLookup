import mysql.connector

from mysql.connector import errorcode
from .connection import connection

cursor = connection.cursor()

def find(queryTerm):
    stringQuery = """'{input}'""".format(input=queryTerm)
    searchQuery = "SELECT * FROM Dictionary WHERE Expression={query}".format(query=stringQuery)
    print(searchQuery)
    try: 
        cursor.execute(searchQuery)
        rows=cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        return err

def create(exp,definition):
    addQuery = "INSERT INTO Dictionary(Expression,Definition) VALUES ('{exp}','{definition}')".format(exp=exp,definition=definition)
    print(addQuery)
    try: 
        cursor.execute(addQuery)
        connection.commit()
        id = cursor.lastrowid
        return id
    except mysql.connector.Error as err:
        return err

def update(exp,updateData):
    print(exp,updateData)
    updateQuery = (
        "Update Dictionary SET Expression='%s',Definition='%s' " 
        "WHERE Expression='%s'") % (*updateData,exp)
    print(updateQuery)
    try: 
        cursor.execute(updateQuery)
        rowsUpdated = cursor.rowcount
        connection.commit()
        return rowsUpdated
    except mysql.connector.Error as err:
        return err

def delete(id):
    deleteQuery = """Delete FROM Dictionary WHERE id={idVal}""".format(idValue=id)
    print(deleteQuery)
    try: 
        cursor.execute(deleteQuery)
        connection.commit()
        id = cursor.deleteid
        return id
    except mysql.connector.Error as err:
        return err

def end():
    cursor.close()