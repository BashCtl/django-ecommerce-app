from django.forms import ModelForm, CharField, Textarea
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    description = CharField(
        widget=Textarea(), label='How can we help you, dude?')

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control my-2'
        self.fields['email'].widget.attrs['class'] = 'form-control my-2'
        self.fields['description'].widget.attrs['class'] = 'form-control my-2'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control my-2'
