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

    def __str__(self):
        name = self.first_name
        # email=self.prof_img
        return name
