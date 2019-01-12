import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
try:
    import local_settings
    SENDER = local_settings.SENDER
    PASSWORD = local_settings.PASSWORD
except ModuleNotFoundError:
    SENDER = "test@email.com"
    PASSWORD = "top-secret password"

server.login(SENDER, PASSWORD)
sender = SENDER


def send_mail(movies, recipients):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "New Movies"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    with open('mail.html') as file:
        html = file.read()

    template = Template(html)
    html = template.render(movies=movies)

    part1 = MIMEText(html, 'html')

    msg.attach(part1)

    server.sendmail(sender, recipients, msg.as_string())
    server.quit()
