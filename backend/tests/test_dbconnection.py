import os 
from sqlalchemy import create_engine 
from sqlalchemy.exc import OperationalError #exception object that indicates database operation issue
from dotenv import load_dotenv 

load_dotenv(dotenv_path=r'C:\Users\arlci\Documents\DEV\Portfolio\DevilDex\backend\.env')

DATABASE_URL = os.getenv("DATABASE_URL")

print(DATABASE_URL)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection: #creates db connection and ensures connection is properly closed
        print('Connected to Devil Fruit database successfully!')
except Exception as e: #handles the exception
    print('Unable to connect to Devil Fruit database.')