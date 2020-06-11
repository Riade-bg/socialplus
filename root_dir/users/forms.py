from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label='', widget=TextInput(attrs={'class':'input-form','placeholder': 'Enter Username'}))
    password = forms.CharField(label='', widget=PasswordInput(attrs={'class':'input-form','placeholder':'Enter Password'}))


class UserRegestraionForm(UserCreationForm):
    email = forms.EmailField(label='',widget=TextInput(attrs={'class':'input-form','placeholder': 'Enter Your Email'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
           raise ValidationError("Email exists")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserRegestraionForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Your Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter Your Password Again'
        
        fields = [
            'username',
            'password1',
            'password2'
        ]
        for index in fields:
            self.fields[index].widget.attrs['class'] = 'input-form'
            self.fields[index].label = False



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='',widget=TextInput(attrs={'class':'input-form'}), required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = False

