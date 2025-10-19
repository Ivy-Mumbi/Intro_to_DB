# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

# Configuration for your MySQL Server connection
# NOTE: Replace 'your_username' and 'your_password' with your actual MySQL credentials
# The database name will be specified later in the script
CONFIG = {
    'user': 'your_username', 
    'password': 'your_password',
    'host': 'localhost'  # Use your host address if it's not localhost
}

DATABASE_NAME = "alx_book_store"


def create_database():
    """Connects to MySQL and creates the specified database."""
    conn = None  # Initialize connection to None
    cursor = None # Initialize cursor to None

    try:
        # 1. Connect to the MySQL server (without specifying a database)
        conn = mysql.connector.connect(**CONFIG)
        cursor = conn.cursor()
        
        print(f"Successfully connected to MySQL server as user '{CONFIG['user']}'.")

        # 2. Execute the CREATE DATABASE statement
        # The 'IF NOT EXISTS' clause prevents the script from failing if the database already exists.
        CREATE_DB_QUERY = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        
        cursor.execute(CREATE_DB_QUERY)
        
        # 3. Print success message (since we can't use SELECT/SHOW, we assume success)
        # Note: In a real-world scenario, you might check cursor.rowcount or use a SHOW statement, 
        # but the IF NOT EXISTS makes the execution safe and the required print message simple.
        print(f"Database '{DATABASE_NAME}' created successfully or already exists.")


    except mysql.connector.Error as err:
        # Handle specific MySQL errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERROR: Failed to connect to DB. Something is wrong with your user name or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"ERROR: Database '{DATABASE_NAME}' does not exist.")
        else:
            print(f"ERROR: An unknown MySQL error occurred: {err}")
    
    except Exception as e:
        # Handle other non-MySQL errors (e.g., local connection issues)
        print(f"ERROR: Failed to connect to the DB. Check your connection parameters or MySQL service status: {e}")

    finally:
        # 4. Handle open and close of the DB connection and cursor
        if cursor:
            cursor.close()
            # print("Cursor closed.")
        if conn and conn.is_connected():
            conn.close()
            # print("Connection closed.")

if __name__ == "__main__":
    create_database()