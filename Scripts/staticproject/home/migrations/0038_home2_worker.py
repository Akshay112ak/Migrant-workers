# Generated by Django 4.2.2 on 2023-09-07 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_home9_working_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='home2',
            name='Worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.home1'),
        ),
    ]