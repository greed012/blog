# Generated by Django 3.2.8 on 2021-11-02 07:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20211102_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_data',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
