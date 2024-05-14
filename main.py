from employee import Employee
from employee_management import EmployeeManagementSystem
from human_resource import HumanResourceModule
from payroll import PayrollSystem
from email_notification import EmailNotification

def main():
    # Configurar el remitente de correo electrónico
    sender_email = 'becerrajosemiguel639@gmail.com'
    sender_password = 'Josemiguel1602.'

    # Crear instancia del sistema de gestión de empleados
    employee_management_system = EmployeeManagementSystem()

    # Crear instancia del módulo de recursos humanos
    hr_module = HumanResourceModule(employee_management_system)

    # Crear instancia del sistema de nóminas
    payroll_system = PayrollSystem(employee_management_system)

    # Crear instancia del sistema de notificación por correo electrónico
    email_notification = EmailNotification(sender_email, sender_password)

    # Lógica de la aplicación
    # Por ejemplo:
    recipient_email = 'josemiguel643152@gmail.com'
    subject = 'Prueba'
    message = 'Este es un mensaje prueba'

    email_notification.send_email_notification(recipient_email, subject, message)

if __name__ == "__main__":
    main()