# Generated by Django 4.2.2 on 2023-07-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_home10'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='user_type',
            field=models.CharField(default='agency', max_length=255),
        ),
        migrations.AddField(
            model_name='home1',
            name='user_type',
            field=models.CharField(default='worker', max_length=255),
        ),
        migrations.AddField(
            model_name='home2',
            name='user_type',
            field=models.CharField(default='police', max_length=255),
        ),
        migrations.AddField(
            model_name='home3',
            name='user_type',
            field=models.CharField(default='insuranceagency', max_length=255),
        ),
    ]