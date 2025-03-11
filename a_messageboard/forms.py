from django.forms import ModelForm
from .models import *
from django import forms

class MessageCreateForm(ModelForm):
    class Meta:
        model=Message
        fields=['body']
        widgets={'body':forms.TextInput( {'placeholder': "Enter message dumbass...", 'class':'p-4 text-black', 'maxlength':'2000'})}
class MessageBoardCreateForm(ModelForm):
    class Meta:
        model=MessageBoard
        fields=['name', 'image']
        widgets={'name':forms.TextInput( {'placeholder': "Name of subreddit...", 'class':'p-4 text-black', 'maxlength':'20'})}