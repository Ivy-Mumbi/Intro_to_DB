# MySQLServer.py
# Objective: Create the database 'alx_book_store' in MySQL, handling errors gracefully.

import mysql.connector

def create_database():
    try:
        # Connect to the MySQL server (update credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # Change if your MySQL username differs
            password=""        # Add password if your MySQL server requires it
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle MySQL-specific errors
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Ensure the connection is closed properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
