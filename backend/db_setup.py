import os #module that enables interaction w/ operating system
from dotenv import load_dotenv #function that enables access to .env file content
from sqlalchemy import create_engine #function that enables connection to database
from sqlalchemy.orm import sessionmaker #function that enables interaction w/ database using sessions (aka Python objects)
from sqlalchemy.ext.declarative import declarative_base #function that enables mapping of Python classes in code to tables in DD

load_dotenv() #loads env variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL") #retrieves database URL from .env file

engine = create_engine(DATABASE_URL) #establishes connection to DD database

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) #these parameters dictate the way the session interacts w/ the database
#bind=engine; SessionLocal should only interact w/ databased defined by DATABASE_URL
#autocommit=False; must explicitly call session.commit() to save changes
#autoflush=False; must explicity call session.flush() for code changes to reflect in database

Base = declarative_base() #defines models that will correspond to tables in database