import sqlite3 as sql

class Repo:

    # def __init__(self):
    #     self.conn = sql.connect("records-db")
    #     self.cursor = self.conn.cursor()

    def createTable(self):
        sql_file = open("setup.sql")
        sql_string = sql_file.read()
        conn = sql.connect("records-db")
        cursor = conn.cursor()
        cursor.executescript(sql_string)
        return cursor.execute("SELECT name from sqlite_master").fetchall()

    def runQuery(self, query):
        conn = sql.connect("records-db")
        cursor = conn.cursor()
        data = cursor.execute(query)
        conn.commit()
        return data
    
    def commitChanges(self):
        self.conn.commit()