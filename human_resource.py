from employee_management import EmployeeManagementSystem

class HumanResourceModule:
    def __init__(self, employee_management_system):
        self.employee_management_system = employee_management_system

    def hire_employee(self, employee):
        self.employee_management_system.add_employee(employee)

    def update_employee_info(self, employee_id, new_data):
        self.employee_management_system.update_employee(employee_id, new_data)

    def fire_employee(self, employee_id):
        self.employee_management_system.delete_employee(employee_id)

    def grant_permissions(self, employee_id, permissions):
        pass

    def assign_roles(self, employee_id, roles):
        pass