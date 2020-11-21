from django.conf import settings
from django.core.mail import send_mail


def email_notification(email, blog, url):
    subject = f'{blog} has released a new post'
    message = f'More details on the link: {url}'
    email_from = settings.EMAIL_HOST_USER
    email_to = [email]
    send_mail(subject, message, email_from, email_to, fail_silently=False)
