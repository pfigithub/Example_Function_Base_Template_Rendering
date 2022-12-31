from django import forms
from app1.models import Contact, Newsletter

class ContactForm(forms.ModelForm):

    class Meta:
        forms = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        forms = Contact
        fields = '__all__'
