import mysql.connector
import os

def db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("HOST", "localhost"),
        user=os.getenv("MYSQL_USERNAME", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "crypto_db")
    )

    return conn