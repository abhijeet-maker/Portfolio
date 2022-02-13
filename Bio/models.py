from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(default=None)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    address = models.CharField(max_length=200, default=None)

    phone = models.CharField(max_length=200, unique=True)

    # phone=models.IntegerField(default=None)

    mail = models.CharField(max_length=30, default=None)
    prof_img = models.ImageField(upload_to='profile_pic/', default=None)
    about = models.TextField(max_length=500, default=None)

    #College

    university=models.TextField(max_length=20, default=None)
    degree=models.TextField(max_length=20, default=None)
    degree_specialisations=models.TextField(max_length=50, default=None)
    degree_cgpa=models.DecimalField(max_digits=3,decimal_places=1)
    degree_date=models.DateField()

    # Intermediate School Detail

    intermediate=models.TextField(max_length=30, default=None)
    intermediate_specialisations=models.TextField(max_length=50, default=None)
    intermediate_percentage=models.DecimalField(max_digits=4,decimal_places=2)
    intermediate_date=models.DateField()

    #School Detail
    matriculation=models.TextField(max_length=30, default=None)
    #matriculation_specialisations=models.TextField(max_length=500, default=None)
    matriculation_percentage=models.DecimalField(default=8.8,max_digits=2,decimal_places=1)
    matriculation_date=models.DateField()

    #Exprience

    job_profile=models.TextField(max_length=20, default=None)
    organisation=models.TextField(max_length=20, default=None)
    job_description=models.TextField(max_length=20, default=None)
    job_duration=models.TextField(max_length=20, default=None)

def __str__(self):
    name = self.first_name
    # email=self.prof_img
    return name
