from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(default=1)
    first_name = models.CharField(max_length=200, default="Abhijeet")
    last_name = models.CharField(max_length=200, default="Kumar")
    address = models.TextField(default="SECTOR 63, NOIDA, UTTAR PRADESH, INDIA")

    phone = models.CharField(max_length=200, unique=True,default=9950124864)

    # phone=models.IntegerField(default=None)

    mail = models.CharField(max_length=30, default="MI01071997GMAIL.COM")
    prof_img = models.ImageField(upload_to='profile_pic/', default=None)
    about = models.TextField(default=None)

    #College

    university=models.TextField(max_length=100, default="GANDHI INSTITUTE OF ENGINEERING AND TECHNOLOGY, GUNUPUR")
    degree=models.TextField(max_length=100, default="GRADUATION (B. TECH)")
    degree_specialisations=models.TextField(max_length=100, default="Electronics & Communication Engineering")
    degree_cgpa=models.DecimalField(max_digits=3,decimal_places=1,default=7.5)
    degree_date=models.DateField()

    # Intermediate School Detail

    intermediate=models.TextField(max_length=100, default="NEW HORIZON SCHOOL, BHAGALPUR")
    intermediate_specialisations=models.TextField(max_length=100, default="SCIENCE (PCM)")
    intermediate_percentage=models.DecimalField(max_digits=4,decimal_places=2,default=65.00)
    intermediate_date=models.DateField()

    #School Detail
    matriculation=models.TextField(max_length=100, default="DAV PUBLIC SCHOOL, CANTT. GAYA")
    #matriculation_specialisations=models.TextField(max_length=500, default=None)
    matriculation_percentage=models.DecimalField(default=8.8,max_digits=2,decimal_places=1)
    matriculation_date=models.DateField()

    #Exprience

    job_profile=models.TextField(max_length=1000, default="QUALITY ENGINEER")
    organisation=models.TextField(max_length=1000, default="CAVISSON SYSTEMS INC")
    job_description=models.TextField(default="QA Automation/Python Developer")
    job_duration=models.TextField(max_length=200, default="09/2019 - Present")
    os=models.TextField(default="Windows, Linux Server, Ubuntu")
    language=models.TextField(default="C, Python, Linux, Java, HTML, CSS")
    database=models.TextField(default="Postgres")
    tools=models.TextField(default="Selenium, Bugzilla, Jira, Wireshark, Ansible")
    framework=models.TextField(default="BDD, Django")
    methodology=models.TextField(default="Agile, DevOps")
    achievements=models.TextField(default=None,help_text="Mention all achievements in newlines.")

    def __str__(self):
        name = self.first_name
        # email=self.prof_img
        return name
