from django.forms import ModelForm
from .models import Search
from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=120, label='Search')