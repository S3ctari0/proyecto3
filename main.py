import schedule
import time
from email_notification import EmailNotification
from employee_management import EmployeeManagementSystem

def enviar_informacion_clientes():
    # Crear instancia del sistema de gestión de empleados
    employee_management_system = EmployeeManagementSystem()

    # Obtener la lista de empleados
    employees = employee_management_system.list_employees()

    # Configurar el remitente de correo electrónico
    sender_email = 'becerrajosemiguel639@gmail.com'
    sender_password = 'kdes pbho iidj ycvj'

    # Crear instancia del sistema de notificación por correo electrónico
    email_notification = EmailNotification(sender_email, sender_password)

    # Iterar sobre la lista de empleados y enviar la información a cada uno
    for employee in employees:
        recipient_email = employee.email
        subject = 'Información del cliente'
        message = f'Hola {employee.name}, aquí está tu información: {employee}'
        email_notification.send_email_notification(recipient_email, subject, message)
        print(f"Correo electrónico enviado a {recipient_email}")

# Programar el envío del correo electrónico todos los días a las 6pm hora colombiana
schedule.every().day.at("18:00").do(enviar_informacion_clientes)

# Mantener el script en ejecución para que schedule pueda ejecutar las tareas programadas
while True:
    schedule.run_pending()
    time.sleep(1)
