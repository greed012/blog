# Generated by Django 3.2.8 on 2021-11-02 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_blog_data_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_data',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
