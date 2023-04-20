#!/usr/bin/python3
""" 
a script that lists all states with a name 
starting with N (upper N) from the database 
hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute query to get states starting with N
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Print the results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()
