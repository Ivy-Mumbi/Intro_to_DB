# MySQLServer.py
# Objective: Create the database 'alx_book_store' in MySQL, handling errors gracefully.

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server (update user and password if necessary)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # Change this if you use a different MySQL user
            password=""        # Add your MySQL password if set
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection to avoid resource leaks
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
