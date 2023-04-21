#!/usr/bin/python3
""" 
a script that lists all states with a name 
starting with N (upper N) from the database 
hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    connect = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connect.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = cursor.fetchall()

    for row in rows_selected:
        print(row)
