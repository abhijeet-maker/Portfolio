# Generated by Django 4.0.1 on 2022-01-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bio', '0006_alter_user_prof_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(default=None, max_length=500),
        ),
    ]
