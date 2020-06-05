from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms.widgets import TextInput


class PostCreateForm(forms.ModelForm):
    post_image = forms.ImageField(label='',widget=forms.FileInput(attrs={'class':'input_file'}))
    class Meta:
        model = PostCreate
        fields = ['post_image']
    
