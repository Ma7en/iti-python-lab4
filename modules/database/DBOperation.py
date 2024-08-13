import psycopg2
import sys

superuser_host = "localhost"
superuser_database_name = "postgres"
superuser_name = "postgres"
superuser_password = "mazen@@1"


# Step 1: connect superuser database
def connect_superuser_db():
    try:
        connection = psycopg2.connect(
            host=superuser_host,
            database=superuser_database_name,
            user=superuser_name,
            password=superuser_password,
        )
        connection.autocommit = True

        print("#" * 50)
        print("Connected to the superuser database successfully")
        print("#" * 50)
        return connection

    except Exception as error:
        print(f"Error while connecting to PostgreSQL:- {error}")
        return None


# Step 2: Create User
def create_user(username, password):  # python, mazen@@1
    try:
        connection = connect_superuser_db()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(f"CREATE USER {username} WITH PASSWORD '{password}';")

        print("#" * 50)
        print(f"User ({username}) created successfully.")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error creating user:- {error}")


# Step 3: Create Database
def create_database(namedatabase, ownername):  # iti_python_lab4, python
    try:
        connection = connect_superuser_db()
        if connection is None:
            return
        cursor = connection.cursor()

        cursor.execute(f"CREATE DATABASE {namedatabase} OWNER {ownername};")
        print("#" * 50)
        print(f"Database ({namedatabase}) created successfully.")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error creating database:- {error}")


# Step 4: privileges database
def grant_privileges_db(database, username):  # iti_python_lab4, python
    try:
        connection = connect_superuser_db()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {database} TO {username};")

        print("#" * 50)
        print(f"Granted all privileges on the database to user ({username}).")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error granting privileges database:- {error}")


# Step 5: Create Connection
user_host = "localhost"
user_database_name = "iti_python_lab4"
user_name = "python"
user_password = "mazen@@1"


def connect_db():
    try:
        connection = psycopg2.connect(
            host=user_host,
            database=user_database_name,
            user=user_name,
            password=user_password,
        )

        print("#" * 50)
        print("Connected to the database successfully")
        print("#" * 50)
        return connection

    except Exception as error:
        print(f"Error while connecting to PostgreSQL:- {error}")
        return None


# Step 6: Create Table Track
def create_table_track():
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        insert_query = f"CREATE TABLE track (id SERIAL PRIMARY KEY, name VARCHAR(100), description TEXT);"
        cursor.execute(insert_query)
        connection.commit()

        print("#" * 50)
        print("The table (track) has been created.")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error creating table track:- {error}")

    finally:
        cursor.close()
        connection.close()


# Step 7: Create Table trainee
def create_table_trainee():
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        insert_query = f"# CREATE TABLE trainee (id SERIAL PRIMARY KEY, name VARCHAR(100), age INT, track_id INT REFERENCES track(id));"
        cursor.execute(insert_query)
        connection.commit()

        print("#" * 50)
        print("The table (trainee) has been created.")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error creating table trainee:- {error}")

    finally:
        cursor.close()
        connection.close()


# Step 8: privileges tables
def grant_privileges_table(table, username):  # (trainee, tarck), python
    try:
        connection = connect_superuser_db()
        if connection is None:
            return
        cursor = connection.cursor()

        cursor.execute(
            f"GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE {table} TO {username};"
        )
        print("#" * 50)
        print(f"Granted INSERT, UPDATE, SELECT, DELETE on tables to user ({username}).")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error granting privileges table:- {error}")


# Step 9: privileges sequence
def grant_privileges_sequence(table, username):  # (trainee, tarck), python
    try:
        connection = connect_superuser_db()
        if connection is None:
            return
        cursor = connection.cursor()

        cursor.execute(f"GRANT USAGE, SELECT ON SEQUENCE {table}_id_seq TO {username};")
        print("#" * 50)
        print(f"Granted USAGE, SELECT on sequences to user ({username}).")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error granting privileges sequence:- {error}")


# Step 10: privileges schema
def grant_privileges_schema(username):  # python
    try:
        connection = connect_superuser_db()
        if connection is None:
            return
        cursor = connection.cursor()

        cursor.execute(
            f"GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {username};"
        )
        print("#" * 50)
        print(
            f"Granted all privileges on all tables in schema public to user ({username})."
        )
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error granting privileges schema:- {error}")


# Step 11: insert table track
def insert_table_track(name, description):  # 'java', 'iti java'
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        insert_query = (
            f"insert into track (name, description) values ('{name}', {description});"
        )
        cursor.execute(insert_query)
        connection.commit()

        print("#" * 50)
        print("Track inserted")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error Inserting Table Track:- {error}")

    finally:
        cursor.close()
        connection.close()


# Step 12: insert table trainee
def insert_table_trainee(name, age, track_id):  # 'mazen', 23, 1
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        insert_query = f"insert into trainee (name, age, track_id) values ('{name}', {age}, {track_id});"
        cursor.execute(insert_query)
        connection.commit()

        print("#" * 50)
        print("Trainee inserted")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error inserting trainee:- {error}")

    finally:
        cursor.close()
        connection.close()


# step 13: update table trainee
def update_table_trainee(trainee_id, name, age, track_id):  # 1, 'ahmed', 25, 1
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        update_query = f"UPDATE trainee SET name = '{name}', age = {age}, track_id = {track_id}  WHERE id = {trainee_id};"
        cursor.execute(update_query)
        connection.commit()

        print("#" * 50)
        print(f"trainee with ID {trainee_id} updated.")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error updating trainee:- {error}")

    finally:
        cursor.close()
        connection.close()


# Step 14: select table trainee
def select_table_trainee():  #
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        select_query = "SELECT * FROM trainee;"
        cursor.execute(select_query)
        employees = cursor.fetchall()

        print("#" * 50)
        for employee in employees:
            print(f"# {employee}")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error selecting trainee: {error}")

    finally:
        cursor.close()
        connection.close()


# Step 15: delete table trainee
def delete_table_trainee(trainee_id):  # 1
    connection = connect_db()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        delete_query = f"DELETE FROM trainee WHERE id = {trainee_id};"
        cursor.execute(delete_query)
        connection.commit()

        print("#" * 50)
        print(f"Employee with ID {trainee_id} deleted.")
        print("#" * 50)

    except psycopg2.DatabaseError as error:
        print(f"Error deleting trainee: {error}")

    finally:
        cursor.close()
        connection.close()
