#!/usr/bin/python3
""" 
a script that lists all states from 
the database hbtn_0e_0_usa 
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM states")

    rows_selected = cursor.fetchall()

    for row in rows_selected:
        print(row)
