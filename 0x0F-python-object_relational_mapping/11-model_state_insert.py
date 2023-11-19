#!/usr/bin/python3
"""
import modules
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database):
    """
    add a new state object to the database
    """
    # Create a database engine
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)
    session.commit()  # Commit changes to the database to persist the new state

    # Print the newly created state's ID
    print(new_state.id)

    # Close the session
    session.close()

if __name__ == "__main__":
    """
    execute program
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        add_state(username, password, database)
