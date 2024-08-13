class Human:
    """
    Human class with instance variables name and age.

    Methods:
        speak: Returns a string that says "Hello, my name is [name] and I am [age] years old."
        introduce: Returns a string that introduces the human.
        get_class_var: Returns the class variable "Human Class Variable" with "edit." appended.

    """

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


class Employee:
    """
    Employee class with instance variables name, age, and employee_id.

    Methods:
        work: Returns a string that says "Employee [name] with ID [employee_id] is working."
        get_class_var: Returns the class variable "Employee Class Variable" with "edit." appended.

    """

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
