import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def dreate_db_connection():
    db_connection = None
    try:
        db_connection = mysql.connector.connect(
            host=os.getenv("HOST", "localhost"),
            user=os.getenv("MYSQL_USERNAME", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=os.getenv("MYSQL_DATABASE", "crypto_db")
        )
        if db_connection.is_connected():
            print("Database connection successful")
    except Error as e:
        print(f"[DATABASE CONNECTION ERROR]: {e}")
    
    return db_connection