#!/usr/bin/python3
""" 
a script that lists all states with a name 
starting with N (upper N) from the database 
hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
