# Create your models here.
from django.db import models
class registerStudent(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField ()
    course=models.CharField(max_length=100)
    address=models.TextField()
    image = models.ImageField(upload_to="image/", null=True)