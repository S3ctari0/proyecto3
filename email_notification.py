import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailNotification:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email_notification(self, recipient_email, subject, message, attachment=None):
        # Configurar el servidor SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Crear instancia del objeto MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Adjuntar el cuerpo del mensaje
        msg.attach(MIMEText(message, 'plain'))

        # Adjuntar el archivo si se proporciona
        if attachment:
            # Implementa la lógica para adjuntar el archivo al mensaje

        # Iniciar sesión en el servidor SMTP
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Enviar el correo electrónico
            server.send_message(msg)

            # Cerrar la conexión con el servidor SMTP
            server.quit()