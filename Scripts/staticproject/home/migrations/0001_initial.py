# Generated by Django 4.2.2 on 2023-07-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('agencyid', models.CharField(max_length=255)),
                ('contactnumber', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]