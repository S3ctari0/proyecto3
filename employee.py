class Employee:
    def __init__(self, employee_id, name, email, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Email: {self.email}, Position: {self.position}, Salary: {self.salary}"
