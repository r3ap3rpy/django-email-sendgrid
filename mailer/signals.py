from .models import ContactMail
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

@receiver(post_save, sender=ContactMail)
def sendEmail(sender, instance, **kwargs):    
    message = Mail(
    from_email='r3ap3rpy@gmail.com',
    to_emails=['r3ap3rpy@gmail.com',instance.email_address],
    subject=instance.title,
    html_content=instance.description)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)        
        print('Success')
    except Exception as e:
        print(f"Error: {e.message}")