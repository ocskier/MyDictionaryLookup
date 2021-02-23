import mysql.connector

from mysql.connector import errorcode
from .connection import connection

class Database:
    def __init__(self):
        self.conn = connection
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE DATABASE IF NOT EXISTS video_games_db;USE video_games_db;CREATE TABLE games(id INT NOT NULL AUTO_INCREMENT,Name TEXT NOT NULL,Genre TEXT NOT NULL,ESRB_Rating TEXT,Platform TEXT NOT NULL,Publisher TEXT,Developer TEXT,Critic_Score TEXT,User_Score TEXT,Year INT,PRIMARY KEY(id));""")
        self.conn.commit()

    def find(self,queryTerm):
        stringQuery = "{input}".format(input=queryTerm)
        searchQuery = "SELECT * FROM games WHERE Name LIKE '%{query}%'".format(query=stringQuery)
        print(searchQuery)
        self.cursor.execute(searchQuery)
        rows = self.cursor.fetchall()
        return rows
        # except mysql.connector.Error as err:
        #     return err

    def create(self,name,genre,platform):
        addQuery = """INSERT INTO games(Name,Genre,Platform) 
        VALUES ('{name}','{genre}','{platform}')
        """.format(name=name,genre=genre,platform=platform)
        print(addQuery)
        self.cursor.execute(addQuery)
        self.conn.commit()
        id = self.cursor.lastrowid
        return id
        # except mysql.connector.Error as err:
        #     return err

    def update(self,name,updateData):
        print(name,updateData)
        updateQuery = (
            "Update games SET User_Score='%s' " 
            "WHERE Name='%s'") % (*updateData,name)
        print(updateQuery)
        self.cursor.execute(updateQuery)
        rowsUpdated = self.cursor.rowcount
        self.conn.commit()
        return rowsUpdated
        # except mysql.connector.Error as err:
        #     return err

    def delete(self,name):
        deleteQuery = """Delete FROM games WHERE Name={name}""".format(name=name)
        print(deleteQuery)
        self.cursor.execute(deleteQuery)
        self.conn.commit()
        id = self.cursor.deleteid
        return id
        # except mysql.connector.Error as err:
        #     return err

    def end(self):
        self.conn.close()