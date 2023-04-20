#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create engine. Arguments:
    # [1] username
    # [2] password
    # [3] database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured class Session
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State object with name passed as argument
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

