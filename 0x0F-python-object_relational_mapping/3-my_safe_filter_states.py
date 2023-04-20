#!/usr/bin/python3
"""
a script that takes in arguments and 
displays all values in the states table 
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute query to get states with matching name
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Print the results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()

