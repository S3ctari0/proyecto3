from employee import Employee

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def update_employee(self, employee_id, new_data):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                # Actualizar los datos del empleado
                pass

    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)

    def get_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

    def list_employees(self):
        return self.employees