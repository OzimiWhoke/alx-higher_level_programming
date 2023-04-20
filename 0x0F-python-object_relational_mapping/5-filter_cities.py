#!/usr/bin/python3
"""
script that takes in the name of a state 
as an argument and lists all cities of 
that state, using the database hbtn_0e_4_usa
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

    # Execute query to get all cities of the given state
    query = "SELECT cities.id, cities.name, states.name FROM cities\
             JOIN states ON cities.state_id = states.id\
             WHERE states.name=%s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Print the results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()

