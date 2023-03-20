import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(to: str, subject:str, message: str) -> None:
    msg = MIMEMultipart()
    msg['From'] = 'pavelfapanas@yandex.ru'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pavelfapanas@yandex.ru', '')
    server.sendmail('pavelfapanas@yandex.ru', to, msg.as_string())


