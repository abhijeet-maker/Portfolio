# Generated by Django 4.0.1 on 2022-01-25 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mail',
        ),
    ]
