from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import User

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'Portfolio administration'
    site_title = 'Administration'
    index_title= 'Administration'
admin_site = MyAdminSite(name='myadmin')
admin_site.register(User)
