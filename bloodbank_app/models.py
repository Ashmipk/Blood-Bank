from turtle import mode

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_community=models.BooleanField(default=False)

bloodType=(
    ('A+','A+'),
('B+','B+'),
('AB+','AB+'),
('O+','O+'),
('A-','A-'),
('B-','B-'),
('AB-','AB-'),
('O-','O-')
)

Gender=(
    ('Female','Female'),
    ('Male','Male'),
    ('Other','Other')
)


class Customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Customers')
    Name=models.CharField(max_length=255)
    District=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    Phone_No=models.CharField(max_length=10)
    Email_Id=models.EmailField()
    Id_card=models.FileField(upload_to='id')

class bloodbank(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING,primary_key=True,related_name='Bloodbank')
    Name=models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    Gender = models.CharField(max_length=10, choices=Gender)
    BloodType = models.CharField(max_length=10, choices=bloodType)
    District = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Phone_No=models.CharField(max_length=10)
    Email_Id=models.EmailField()
    Id_card=models.FileField(upload_to='id')


class bloodrequest(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='bloodrequest')
     Patient_name=models.CharField(max_length=255)
     BloodType = models.CharField(max_length=10, choices=bloodType)
     no_of_units = models.CharField(max_length=10)
     Bistander_name = models.CharField(max_length=255)
     Phone_No = models.CharField(max_length=10)
     Hsptl_details = models.CharField(max_length=255)
     date_field = models.DateField()
     Donar_Name=models.CharField(max_length=100,null=True,blank=True)
     Donar_Age = models.CharField(max_length=100, null=True, blank=True)
     Donar_BloodType = models.CharField(max_length=100, null=True, blank=True)
     Donar_Location = models.CharField(max_length=100, null=True, blank=True)
     Donar_Number = models.CharField(max_length=100, null=True, blank=True)
     Approval_status = models.IntegerField(default=0)
