from django import forms
from .models import ContactForm_E, ContactForm_I

class ContactFormForm_E(forms.ModelForm):
    class Meta:
        model = ContactForm_E
        fields = ['mbti', 'influence', 'comments']

class ContactFormForm_I(forms.ModelForm):
    class Meta:
        model = ContactForm_I
        fields = ['mbti', 'influence', 'comments']