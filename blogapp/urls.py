from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('createpost/',views.create, name='create'),
    path('detail_view/<int:post_id>',views.details_view, name='details'),
    path('edit_post/<int:post_id>',views.edit, name='edit'),
    path('category/',views.add_category, name='add_category'),
    path('drafts/',views.drafts, name='drafts'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('authentication.urls')),

]