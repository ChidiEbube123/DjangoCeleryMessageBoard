from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
import datetime
@shared_task(name="Email notification")
def send_email_task(subject, body,email_address):
    email=EmailMessage(subject, body, to=[email_address])
    email.send()
    return email_address

@shared_task(name="monthly newsletter")
def send_newsletter_task(subject, body,email_address):
    subject="Your news letter"
    subscribers=MessageBoard.objects.get(id=1).subscribers.all()
    for subscriber in subscribers:
        body=render_to_string('a_messageboard/newsletter.html', {'name':subscriber.profile.name})
        email=EmailMessage(subject, body, to=[subscriber.email])
        email.content_subtype="html"
        email.send()
    current_month=datetime.now().strfrtime('%B')
    subscriber_count=subscribers.count()
    return f"{current_month} newsletter to {subscriber_count} subs"