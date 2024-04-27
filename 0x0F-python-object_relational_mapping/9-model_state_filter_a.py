#!/usr/bin/python3
""" Lists all states containing letter a."""
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3].strip('.')

    details = f"mysql+mysqldb://{username}:{urllib.parse.quote_plus(password)}@localhost:3306/{database}"
    engine = create_engine(details, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for name in session.query(State).filter(State.name.ilike('%a%')).order_by(State.id.asc()):
        print(f"{name.id}: {name.name}")
    session.close()
