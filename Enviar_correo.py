import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Configura tus credenciales y la información del servidor SMTP
smtp_server = 'servidor_smtp'
smtp_port = 465  # Utiliza el puerto 465 para SSL
tu_correo = 'info@correo.com'
tu_contraseña = 'tu_contraseña'
correo_destino = 'vkzqyccl@hldrive.com'
asunto = 'Holis'

# Crea el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = tu_correo
mensaje['To'] = correo_destino
mensaje['Subject'] = asunto

# Agrega el cuerpo del correo
cuerpo = 'Este es el cuerpo del correo.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Si deseas adjuntar un archivo, puedes hacerlo de la siguiente manera
archivo_adjunto = 'archivo.pdf'
with open(archivo_adjunto, 'rb') as f:
    adjunto = MIMEApplication(f.read(), _subtype="pdf")
    adjunto.add_header('Content-Disposition', 'attachment', filename=archivo_adjunto)
    mensaje.attach(adjunto)

# Conéctate al servidor SMTP utilizando SSL y envía el correo
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(tu_correo, tu_contraseña)
    server.sendmail(tu_correo, correo_destino, mensaje.as_string())
    server.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print("Error al enviar el correo:", str(e))
