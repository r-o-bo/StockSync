import mysql.connector
from mysql.connector import Error
from database import db_connection

def create_table():
    CREATE_TABLE_SQL_QUERY = ("""
        CREATE TABLE IF NOT EXISTS eth_prices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            symbol VARCHAR(10),
            name VARCHAR(50),
            price DECIMAL(18,8),
            change DECIMAL(18,8),
            percent_change VARCHAR(10),
            volume BIGINT,
            market_cap BIGINT,
            week_high DECIMAL(18,8),
            week_low DECIMAL(18,8),
            logo VARCHAR(255),
            last_updated VARCHAR(50),
            transformed_at DATETIME
        )
    """)
    try:
        cursor = db_connection.cursor()
        cursor.execute(CREATE_TABLE_SQL_QUERY)
        db_connection.commit()
        print("Table created successfully")

    except Error as e:
        print(f"[CREATING TABLE ERROR]: '{e}'")
  