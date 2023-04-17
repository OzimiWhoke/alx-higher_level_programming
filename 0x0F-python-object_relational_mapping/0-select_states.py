#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: python list_states.py <username> <password> <database>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
except MySQLdb.Error as e:
    print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
