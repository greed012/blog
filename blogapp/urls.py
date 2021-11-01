from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('createpost/',views.create, name='create'),
    path('detail_view/<int:post_id>',views.details_view, name='details'),
    path('edit_post/<int:post_id>',views.edit, name='edit'),
    path('category/',views.add_category, name='add_category'),
    path('dashboard/',views.dashboard, name='dashboard'),

]