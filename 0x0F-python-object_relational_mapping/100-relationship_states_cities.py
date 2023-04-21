#!/usr/bin/python3
"""
Create a State object "California" with a City object "San Francisco"
using SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql username> <mysql password> <database name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    ca = State(name='California')

    sf = City(name='San Francisco')

    ca.cities.append(sf)

    session.add(ca)

    session.commit()
    
    session.close()
