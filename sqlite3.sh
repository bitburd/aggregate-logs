#!/bin/bash
# setup a sqlite3 db for db.py script

sqlite3 sqlite3_db "create table items (id INTEGER PRIMARY KEY, data TEXT, item TEXT, date TEXT, time TEXT);"
chmod 664 sqlite3_db
