from django.forms import ModelForm
from .models import ContactMail

class ContactForm(ModelForm):
    class Meta:
        model = ContactMail
        fields = '__all__'