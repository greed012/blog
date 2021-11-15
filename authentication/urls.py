from django.urls import path, include
from . import views

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register')
]