import psycopg2
import sys


# --> create virtualenv
# virtualenv -p python3.12 venv
# source venv/bin/activate

# --> install psycopg
# pip install psycopg2-binary
# pip install --upgrade pip

# --> open postgresql
# su - postgres
# mazen@@1
# psql

# --> create user
# CREATE USER python WITH PASSWORD 'mazen@@1';
# CREATE DATABASE iti_python_lab4;

# --> privileges
# GRANT ALL PRIVILEGES ON DATABASE iti_python_lab4 TO python;

# GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE trainee TO python;
# GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE track TO python;

# GRANT USAGE, SELECT ON SEQUENCE trainee_id_seq TO python;
# GRANT USAGE, SELECT ON SEQUENCE track_id_seq TO python;

# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO python;


# --> remove user from database
# تاكد من حذف كل قواعد البيانات التي للكذلك المستخدم الصلاحية عليها
# DROP USER python;


# --> connact database
# \c iti_python_lab4


# --> create table
# CREATE TABLE track (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     description TEXT
# );

# CREATE TABLE trainee (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INT,
#     track_id INT REFERENCES track(id)
# );

# --> insert table
# insert into
# track
#     (name, description)
# values
#     ('java', 'iti java');


# pg_dump postgres_lab3 > /tmp/postgres_lab3_db.txt
# drop database iti_python_lab4;


# =================================================================
# =================================================================


# step 1: create
def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="iti_python_lab4",
            user="python",
            password="mazen@@1",
        )
        print("#" * 50)
        print("Connected to the database successfully")
        print("#" * 50)
        return connection
    except:
        print(f"Error connecting to the database")
        return None


# continue_db = connect_db()
# print(continue_db())


# step 2: insert
def insert_db(name, age, track_id):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        insert_query = f"insert into trainee (name, age, track_id) values ('{name}', {age}, {track_id});"
        cursor.execute(insert_query)
        # trainee_id = cursor.fetchone()[0]
        connection.commit()
        print("#" * 50)
        # print(f"trainee insert with ID: {trainee_id}")
        print("insert")
        print("#" * 50)
    except psycopg2.DatabaseError as e:
        print(f"Error inserting trainee: {e}")
    finally:
        cursor.close()
        connection.close()


# insert_db("mazen", 23, 1)


# step 3: update
def update_db(trainee_id, name, age, track_id):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        update_query = f"UPDATE trainee SET name = '{name}', age = {age}, track_id = {track_id}  WHERE id = {trainee_id};"
        cursor.execute(update_query)
        connection.commit()
        print(f"trainee with ID {trainee_id} updated.")
    except psycopg2.DatabaseError as e:
        print(f"Error updating trainee: {e}")
    finally:
        cursor.close()
        connection.close()


# update_db(3, "saad", 25, 1)


# step 4: select
def select_db():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        select_query = "SELECT * FROM trainee;"
        cursor.execute(select_query)
        employees = cursor.fetchall()

        for employee in employees:
            print(f"# {employee}")
    except:
        print(f"Error select trainee")
    finally:
        cursor.close()
        connection.close()


# select_db()


# step 5: delete
def delete_db(trainee_id):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        delete_query = f"DELETE FROM trainee WHERE id = {trainee_id};"
        cursor.execute(delete_query)
        connection.commit()

        print(f"Employee with ID {trainee_id} deleted.")
    except:
        print(f"Error deleting trainee")
    finally:
        cursor.close()
        connection.close()


# delete_db(3)


# =================================================================================================
# =================================================================================================


class Human:
    class_var = "Human Class Variable"

    def __init__(self, name, age):
        self.instance_var_name = name
        self.instance_var_age = age

    def speak(self):
        return f"({self.instance_var_name}) says hello!"

    def introduce(self):
        return f"Hello, my name is ({self.instance_var_name}) and I am ({self.instance_var_age}) years old."

    @classmethod
    def get_class_var(cls):
        return cls.class_var + " edit."


mazen_HU = Human("mazen", 23)
print(mazen_HU.speak())
print(mazen_HU.introduce())
print(mazen_HU.get_class_var())


class Employee:
    class_var = "Employee Class Variable"

    def __init__(self, name, age, employee_id):
        self.instance_var_name = name
        self.instance_var_age = age
        self.instance_var_employee_id = employee_id

    def work(self):
        return f"Employee ({self.instance_var_name}) with ID ({self.instance_var_employee_id}) is working."

    @classmethod
    def get_class_var(cls):
        return cls.class_var + " edit."


mazen_EM = Employee("mazen", 23, 1)
print(mazen_EM.work())
print(mazen_EM.get_class_var())


# =================================================================================================
# =================================================================================================


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance


class Customer:
    def __init__(self, name):
        self.name = name
