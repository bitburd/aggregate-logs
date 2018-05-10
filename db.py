#!/usr/bin/python
# Connect to a db if found and insert item into it
#example: #insert_data("This is the error item data","404","May 8 2018","5:02:00");

import sqlite3

db_file = "./sqlite3_db"
conn = sqlite3.connect(db_file)

def create_connection():
    global conn
    try:
        conn = sqlite3.connect(db_file)
        print "opened database"
        return conn
    except Error as e:
        print(e)
 
    return None

def insert_data(datatext,itemtext,date,time):
    global conn
    sql = ''' INSERT INTO items('data','item','date','time') VALUES('%s','%s','%s','%s') ''' % (datatext,itemtext,date,time)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print "Inserted data"
    return cur.lastrowid

def close_connection():
    global conn
    conn.close()
