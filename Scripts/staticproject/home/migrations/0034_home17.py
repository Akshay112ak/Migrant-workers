# Generated by Django 4.2.2 on 2023-08-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_home16'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home17',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderid', models.IntegerField(null=True)),
                ('recevierid', models.IntegerField(null=True)),
                ('message', models.TextField(max_length=255)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]