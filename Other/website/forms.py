from django.forms import ModelForm
from django.forms import Form
from django import forms
from .models import Product

class ProductForm(ModelForm):
    title = forms.CharField(label = '', widget = forms.TextInput(attrs={"placeholder": "Name"}))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea)
    price       = forms.DecimalField(initial=99.99)
    class Meta:
        model = Product
        fields = [
            'title', 
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "RIADE" in title:
            return title
        else:
            raise forms.ValidationError("This is not valid title")

class RawFormClass(Form):
    title       = forms.CharField(label = '', widget = forms.TextInput(attrs={"placeholder": "Name"}))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea)
    price       = forms.DecimalField(initial=99.99)