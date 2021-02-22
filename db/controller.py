import mysql.connector

from mysql.connector import errorcode
from .connection import connection

cursor = connection.cursor()

def find(queryTerm):
    stringQuery = "{input}".format(input=queryTerm)
    searchQuery = "SELECT * FROM games WHERE Name LIKE '%{query}%'".format(query=stringQuery)
    print(searchQuery)
    try: 
        cursor.execute(searchQuery)
        rows=cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        return err

def create(name,genre,platform):
    addQuery = """INSERT INTO games(Name,Genre,Platform) 
    VALUES ('{name}','{genre}','{platform}')
    """.format(name=name,genre=genre,platform=platform)
    print(addQuery)
    try: 
        cursor.execute(addQuery)
        connection.commit()
        id = cursor.lastrowid
        return id
    except mysql.connector.Error as err:
        return err

def update(name,updateData):
    print(name,updateData)
    updateQuery = (
        "Update games SET User_Score='%s' " 
        "WHERE Name='%s'") % (*updateData,name)
    print(updateQuery)
    try: 
        cursor.execute(updateQuery)
        rowsUpdated = cursor.rowcount
        connection.commit()
        return rowsUpdated
    except mysql.connector.Error as err:
        return err

def delete(name):
    deleteQuery = """Delete FROM games WHERE Name={name}""".format(name=name)
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