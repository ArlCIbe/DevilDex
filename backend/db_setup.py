import os #module that enables interaction w/ operating system
from dotenv import load_dotenv #function that enables access to .env file content
from sqlalchemy import create_engine #function that enables connection to db
from sqlalchemy.orm import sessionmaker #function that enables interaction w/ db using sessions (aka Python objects)
from sqlalchemy.ext.declarative import declarative_base #function that enables mapping of Python classes in code to tables in DD

load_dotenv() #loads env variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL") #retrieves db URL from .env file

engine = create_engine(DATABASE_URL) #establishes connection to DD db

#sessionmaker() parameters dictate the way the session interacts w/ the db
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) 
#bind=engine; SessionLocal should only interact w/ db defined by DATABASE_URL
#autocommit=False; must explicitly call session.commit() to save changes
#autoflush=False; must explicity call session.flush() for code changes to reflect in db

Base = declarative_base() #defines models that will correspond to tables in db