#!/usr/bin/python3
""" Updates the name of a state."""
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]

    details = (
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
            )
    engine = create_engine(details, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_name = session.query(State).filter(State.id == 2).first()

    new_name.name = "New Mexico"
    session.commit()
    session.close()
