# Generated by Django 3.2.8 on 2021-11-11 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_alter_blog_data_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_data',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ip_filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('entered_date', models.DateField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blog_data')),
            ],
        ),
    ]