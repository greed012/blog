from django.forms import ModelForm
from . models import blog_data, category
from django import forms


class blog_data_form(ModelForm):
    class Meta:
        model = blog_data
        fields = ['title', 'author','cover_image', 'body']

        widgets = {
             'title': forms.TextInput(attrs={'class':"form-control"}),
             'author': forms.TextInput(attrs={'class':"form-control"}),
        }

class category_form(ModelForm):
    class Meta:
        model = category
        fields = ['category_name']

        widgets = {
             'category_name': forms.TextInput(attrs={'class':"form-control"}),
        }
