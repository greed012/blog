from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime, date
from django.utils import timezone
# Create your models here.

class category(models.Model):
    cat_number = models.AutoField
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name

class blog_data(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(category,on_delete=models.SET_DEFAULT,default='7')
    published_date = models.DateTimeField(default=timezone.now)
    created_created_date = models.DateTimeField(auto_now_add=True)
    updated_create_date = models.DateTimeField(auto_now=True)
    cover_image = RichTextUploadingField(blank=True, null=True, config_name='cover_image')
    body = RichTextUploadingField(blank=True,null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title + '   |  ' + self.author

class ip_filter(models.Model):
    post = models.ForeignKey(blog_data,on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    entered_date = models.DateField()

    def __str__(self):
        return self.ip_address

class no_views(models.Model):
    post = models.ForeignKey(blog_data,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title