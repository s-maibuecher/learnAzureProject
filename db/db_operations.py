import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def select_count_from_first_row():
    connection = None
    try:
        # Connect to the 'DB_EP_A' database
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
        )

        cursor = connection.cursor()

        # Select the 'Count' value from the first row
        select_query = "SELECT Count FROM endpoint_count LIMIT 1"
        cursor.execute(select_query)

        row = cursor.fetchone()
        if row:
            count_value = row[0]
            print(f"Count value from the first row: {count_value}")
            return count_value
        else:
            print("No rows found in the 'endpoint_count' table.")
            return None

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to 'DB_EP_A':", error)
        return None

    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()


def increment_table_counter(count):
    connection = None
    try:
        # Connect to the 'DB_EP_A' database
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
        )

        cursor = connection.cursor()

        # Select the 'Count' value from the first row
        update_query = f"UPDATE endpoint_count SET Count = {count} + 1 WHERE ID = 1"
        cursor.execute(update_query)

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to 'DB_EP_A':", error)
        return None

    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()


def create_table_and_insert_row():
    connection = None
    try:
        # Replace the connection parameters with your PostgresSQL database credentials
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
        )

        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS endpoint_count (
            ID SERIAL PRIMARY KEY,
            Count INTEGER
        )
        """
        cursor.execute(create_table_query)

        # Insert one row with Count=0
        insert_row_query = """
        INSERT INTO endpoint_count (Count)
        VALUES (0)
        """
        cursor.execute(insert_row_query)

        connection.commit()
        print(
            "Table 'endpoint_count' created, and one row inserted successfully!",
            flush=True,
        )

    except (Exception, psycopg2.Error) as error:
        print("***" * 20)
        print("Error while connecting to PostgreSQL:", error)

    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
