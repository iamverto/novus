from django.core.mail import EmailMessage
from django.conf import settings

def send_email_for_chatbox(receiver_email_id, subject, name):
    body = 'Thank you for contacting us ' + name + '<br>We will contact you soon! <br>Sinc. <b>Novusorg.com LPU</b>'
    email = EmailMessage(subject=subject, body=body, to=[receiver_email_id])
    email.send()