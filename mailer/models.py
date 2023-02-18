from django.db import models
from uuid import uuid4
# Create your models here.
class ContactMail(models.Model):
    id = models.UUIDField(default=uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False,null=False)
    email_address = models.EmailField(blank=False,null=False)
    def __str__(self):
        return f"From: {self.email_address} :: Title: {self.title}"