################### Q1 ##########################
# *** Database Operations *** #
from modules.database.DBOperation import (
    connect_superuser_db,
    create_user,
    create_database,
    grant_privileges_db,
    connect_db,
    create_table_track,
    create_table_trainee,
    grant_privileges_table,
    grant_privileges_sequence,
    grant_privileges_schema,
    insert_table_track,
    insert_table_trainee,
    update_table_trainee,
    select_table_trainee,
    delete_table_trainee,
)

# -- p1 --
# print(connect_superuser_db())


# -- p2 --
# insert_db("ahemd", 23, 1)


# -- p3 --
# update_db(3, "saad", 25, 1)


# -- p4 --
# select_db()


# -- p5 --
# delete_db(3)


# -- p6 --


# -- p7 --


# -- p8 --


# -- p9 --


# -- p10 --


# -- p11 --


# -- p12 --


# -- p13 --


# -- p14 --


# -- p15 --


################### Q2 ##########################
# from modules.classs.Class import Human, Employee

# -- p1 --
# mazen_HU = Human("mazen", 23)
# print(mazen_HU.speak())
# print(mazen_HU.introduce())
# print(mazen_HU.get_class_var())


# -- p2 --
# mazen_EM = Employee("mazen", 23, 1)
# print(mazen_EM.work())
# print(mazen_EM.get_class_var())


################### Q3 - Bunce ##########################
# from modules.classs.Bank import Bank, Account, Customer
