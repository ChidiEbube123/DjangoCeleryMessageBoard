from django.forms import ModelForm
from .models import *
from django import forms

class MessageCreateForm(ModelForm):
    class Meta:
        model=Message
        fields=['body']
        widgets={'body':forms.TextInput( {'placeholder': "Enter message dumbass...", 'class':'p-4 text-black', 'maxlength':'2000'})}