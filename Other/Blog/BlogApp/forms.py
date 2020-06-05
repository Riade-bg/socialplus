from django.forms import ModelForm
from .models import Article
from django import forms

class ArticleForm(ModelForm):
    title = forms.CharField(max_length=120, label='Title', widget=forms.TextInput(attrs={"placeholder":"Enter Title"}))
    class Meta:
        model = Article
        fields= [
            'title',
            'content',
            'active'
        ]
