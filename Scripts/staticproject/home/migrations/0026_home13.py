# Generated by Django 4.2.2 on 2023-08-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_home7_currentdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home13',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CURRENTDATE', models.DateField(null=True)),
                ('file', models.FileField(upload_to='uploads/')),
                ('Scheme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.schome')),
                ('Worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.home1')),
            ],
        ),
    ]
