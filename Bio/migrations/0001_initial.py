# Generated by Django 4.0.1 on 2022-02-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None)),
                ('first_name', models.CharField(default=None, max_length=200)),
                ('last_name', models.CharField(default=None, max_length=200)),
                ('address', models.CharField(default=None, max_length=200)),
                ('phone', models.CharField(max_length=200, unique=True)),
                ('mail', models.CharField(default=None, max_length=30)),
                ('prof_img', models.ImageField(default=None, upload_to='profile_pic/')),
                ('about', models.TextField(default=None, max_length=500)),
                ('university', models.TextField(default=None, max_length=500)),
                ('degree', models.TextField(default=None, max_length=20)),
                ('degree_specialisations', models.TextField(default=None, max_length=50)),
                ('degree_cgpa', models.DecimalField(decimal_places=1, max_digits=3)),
                ('degree_date', models.DateField()),
                ('intermediate', models.TextField(default=None, max_length=500)),
                ('intermediate_specialisations', models.TextField(default=None, max_length=50)),
                ('intermediate_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('intermediate_date', models.DateField()),
                ('matriculation', models.TextField(default=None, max_length=500)),
                ('matriculation_percentage', models.DecimalField(decimal_places=1, default=8.8, max_digits=2)),
                ('matriculation_date', models.DateField()),
            ],
        ),
    ]
