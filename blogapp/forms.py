from django.forms import ModelForm
from . models import blog_data
from django import forms


class blog_data_form(ModelForm):
    class Meta:
        model = blog_data
        fields = ['title', 'author', 'body']

        widgets = {
             'title': forms.TextInput(attrs={'class':"form-control"}),
             'author': forms.TextInput(attrs={'class':"form-control"}),
        }