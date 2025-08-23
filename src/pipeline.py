from database import create_db_connection
from load import create_table, insert_into_table
from transform import transform_data
from extract import my_crypto_summary
from api_config import check_rate_lim

def run_data_pipeline():
    # Check API rate limits before running extraction
    check_rate_lim()

    conn = create_db_connection()
    if not conn:
        print("Failed to establish database connection. Exiting pipeline.")
        return
    
    try:
        # Create table if it doesn’t exist
        create_table(conn)

        # Extract
        summary = my_crypto_summary()
        if summary:
            # Transform
            df = transform_data(summary)

            # Load
            insert_into_table(conn, df)
            print("Data pipeline executed successfully!")
        else:
            print("No data extracted from API. Skipping transform/load step.")

    except Exception as e:
        print(f"Error in pipeline: {e}")

    finally:
        conn.close()
        print("🔒 Database connection closed.")


if __name__ == "__main__":
    run_data_pipeline()
