#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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

    # Execute query to get all cities
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)

    # Print the results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()
