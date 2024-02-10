from django.contrib import admin
from .models import Employee, Work, Assignment
# Register your models here.

admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Assignment)