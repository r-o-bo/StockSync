import mysql.connector
from mysql.connector import Error
from config.database import create_db_connection

def create_table(db_connection):
    CREATE_TABLE_SQL_QUERY = ("""
    CREATE TABLE IF NOT EXISTS eth_prices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        symbol VARCHAR(10),
        name VARCHAR(50),
        price DECIMAL(18,8),
        price_change DECIMAL(18,8),
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
    finally:
        cursor.close()
        print("Database cursor closed.")
        

def insert_into_table(db_connection, df):
    """
    Insert data in the database from the dataframe
    """
    cursor = db_connection.cursor()

    INSERT_DATA_SQL_QUERY = """
        INSERT INTO eth_prices (
        symbol,
        name,
        price,
        price_change,
        percent_change,
        volume,
        market_cap,
        week_high,
        week_low,
        logo,
        last_updated,
        transformed_at
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # this creates a list of tuples from the dataframe values
    data_values_as_tuples = [tuple(x) for x in df.to_numpy()]

    # Execute the query
    try:
        cursor.executemany(INSERT_DATA_SQL_QUERY, data_values_as_tuples)
        db_connection.commit()
        print("Data inserted or updated successfully!")
    except Error as e:
        print(f"[INSERT ERROR]: {e} ")
    finally:
        cursor.close()
    
    