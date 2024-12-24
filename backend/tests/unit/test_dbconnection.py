import os 
from dotenv import load_dotenv
import psycopg 

load_dotenv() #loads the .env file into the script's environment

DATABASE_URL = os.getenv("DATABASE_URL")

print(DATABASE_URL)

try:
    with psycopg.connect(DATABASE_URL) as conn: #creates db connection; with ensures connection gets closed properly & conn object enables interaction w/ db

        with conn.cursor() as cur: #creates cur object; used to execute SQL queries against the db

            cur.execute('SELECT 1 FROM devilfruits') #returns the number 1

            result = cur.fetchall() #retrieves the 1st result from the query
            
            print(f"Query result: {result} - Connected to Devil Fruit database successfully!")

except Exception as e: #handles the exception
    print(f"Unable to connect to Devil Fruit database: {e}")