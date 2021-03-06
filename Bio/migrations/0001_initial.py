# Generated by Django 4.0.1 on 2022-02-16 06:32

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
                ('user_id', models.IntegerField(default=1)),
                ('first_name', models.CharField(default='Abhijeet', max_length=200)),
                ('last_name', models.CharField(default='Kumar', max_length=200)),
                ('address', models.TextField(default='SECTOR 63, NOIDA, UTTAR PRADESH, INDIA')),
                ('phone', models.CharField(default=9950124864, max_length=200, unique=True)),
                ('mail', models.CharField(default='MI01071997GMAIL.COM', max_length=32)),
                ('prof_img', models.ImageField(default=None, upload_to='static/Bio/assets/img/')),
                ('about', models.TextField(default=None)),
                ('university', models.TextField(default='GANDHI INSTITUTE OF ENGINEERING AND TECHNOLOGY, GUNUPUR', max_length=100)),
                ('degree', models.TextField(default='GRADUATION (B. TECH)', max_length=100)),
                ('degree_specialisations', models.TextField(default='Electronics & Communication Engineering', max_length=100)),
                ('degree_cgpa', models.DecimalField(decimal_places=1, default=7.5, max_digits=3)),
                ('degree_date', models.DateField()),
                ('intermediate', models.TextField(default='NEW HORIZON SCHOOL, BHAGALPUR', max_length=100)),
                ('intermediate_specialisations', models.TextField(default='SCIENCE (PCM)', max_length=100)),
                ('intermediate_percentage', models.DecimalField(decimal_places=2, default=65.0, max_digits=4)),
                ('intermediate_date', models.DateField()),
                ('matriculation', models.TextField(default='DAV PUBLIC SCHOOL, CANTT. GAYA', max_length=100)),
                ('matriculation_percentage', models.DecimalField(decimal_places=1, default=8.8, max_digits=2)),
                ('matriculation_date', models.DateField()),
                ('job_profile', models.TextField(default='QUALITY ENGINEER', max_length=1000)),
                ('organisation', models.TextField(default='CAVISSON SYSTEMS INC', max_length=1000)),
                ('job_description', models.TextField(default='QA Automation/Python Developer')),
                ('job_duration', models.TextField(default='09/2019 - Present', max_length=200)),
                ('os', models.TextField(default='Windows, Linux Server, Ubuntu')),
                ('language', models.TextField(default='C, Python, Linux, Java, HTML, CSS')),
                ('database', models.TextField(default='Postgres')),
                ('tools', models.TextField(default='Selenium, Bugzilla, Jira, Wireshark, Ansible')),
                ('framework', models.TextField(default='BDD, Django')),
                ('methodology', models.TextField(default='Agile, DevOps')),
                ('achievements', models.TextField(default=None, help_text='Mention all achievements in newlines.')),
            ],
        ),
    ]
