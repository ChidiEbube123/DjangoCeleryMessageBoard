'''from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
@receiver(post_save, sender=Message)
def send_email(sender,instance,created,**kwargs):
    message=instance
    site_domain=Site.objects.get(pk=1).domain
    if created:
        for sub in message.messageboard.subscribers.all():
            if sub != message.author:
                try:
                    email_address=sub.emailaddress_set.get(primary=True, verified=True)
                    email_subject=f'New Message from {message.author}'
                    email_body=f'Seems like \n you received a new message at {site_domain}'
                    email=EmailMessage(email_subject, email_body, to=[email_address.email])
                    email.send()
                except:
                    pass'''