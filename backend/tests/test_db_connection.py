import os 
from sqlalchemy import create_engine 
from sqlalchemy.exc import OperationalError #exception object that indicates database operation issue
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection: