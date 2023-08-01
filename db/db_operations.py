import psycopg2


# TODO HIER WEITER, das mal ausprobieren: https://stackoverflow.com/questions/73355454/how-to-connect-python-to-postgres-through-docker-compose
HOST_ADDRESS = 'db'

def select_count_from_first_row():
    connection = None
    try:
        # Connect to the 'DB_EP_A' database
        connection = psycopg2.connect(
            user="stefan",
            password="123",
            host=HOST_ADDRESS,
            port="5432",
            database="postgres"
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
            user="stefan",
            password="123",
            host=HOST_ADDRESS,
            port="5432",
            database="postgres"
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
        # Replace the connection parameters with your PostgreSQL database credentials
        connection = psycopg2.connect(
            user="stefan",
            password="123",
            host=HOST_ADDRESS,
            port="5432",
            database="postgres"
        )

        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS endpoint_count (
            ID SERIAL PRIMARY KEY,
            Count INTEGER
        )
        '''
        cursor.execute(create_table_query)

        # Insert one row with Count=0
        insert_row_query = '''
        INSERT INTO endpoint_count (Count)
        VALUES (0)
        '''
        cursor.execute(insert_row_query)

        connection.commit()
        print("Table 'endpoint_count' created, and one row inserted successfully!", flush=True)

    except (Exception, psycopg2.Error) as error:
        print("***" * 20)
        print("Error while connecting to PostgreSQL:", error)

    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
