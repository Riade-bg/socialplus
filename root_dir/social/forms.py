from django import forms
from django.core.exceptions import ValidationError
from .models import *
from users.models import Profile
from django.forms.widgets import TextInput


class PostCreateForm(forms.ModelForm):
    post_image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class':'file-upload-input', 'type':'file'}))
    class Meta:
        model = PostCreate
        fields = ['post_image']

class ProfilePictureUpdate(forms.ModelForm):
    avatar = forms.ImageField(label='', widget=forms.FileInput(attrs={'class':'profile-update-input', 'type':'file'}))
    class Meta:
        model = Profile
        fields = ['avatar',]
