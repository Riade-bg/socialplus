from django import forms
from .models import *

class MessageVerfication(forms.ModelForm):
    message = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder':'Type a message', 'class':'msg-input'}))
    class Meta:
        model = imessage
        fields = ['message']