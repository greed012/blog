from django.contrib import admin
from . models import blog_data,category,ip_filter, no_views
# Register your models here.
admin.site.register(blog_data)
admin.site.register(category)
admin.site.register(ip_filter)
admin.site.register(no_views)