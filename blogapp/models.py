from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime, date
# Create your models here.

class category(models.Model):
    cat_number = models.AutoField
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name

class blog_data(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    cover_image = RichTextUploadingField(blank=True, null=True, config_name='cover_image')
    body = RichTextUploadingField(blank=True,null=True)


    def __str__(self):
        return self.title + '   |  ' + self.author