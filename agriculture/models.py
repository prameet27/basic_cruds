from django.db import models
from datetime import date
from django.utils.timezone import timedelta

# Create your models here.
class Employee(models.Model):
    emp_id = models.PositiveIntegerField()
    emp_name = models.CharField(max_length = 1000, default = 'default value')
    emp_address_temporary = models.CharField(max_length = 1000)
    emp_address_permanent = models.CharField(max_length = 1000)
    emp_date_of_birth = models.DateField(blank=True, null=True)
    emp_national = models.CharField(max_length = 1000, default = 'default_value')
    emp_email = models.EmailField(max_length = 1000)
    emp_contact_number = models.CharField(max_length=1000)
    emp_image = models.ImageField(upload_to='image/', default='blank-avatar-photo-icon-design-vector-30257190.jpg')

class Work(models.Model):
    work_primary = models.CharField(max_length=1000)
    work_primary_image_stufa=models.ImageField(upload_to='image/')
    work_primary_description=models.CharField(max_length=1000, default='default_value', blank=True, null=True)

class Assignment(models.Model):
    boss_name = models.CharField(max_length=1000)
    emp_name = models.ForeignKey(Employee, null = True, on_delete = models.CASCADE)
    work_primary = models.ForeignKey(Work, null = True, on_delete = models.CASCADE)