from .models import Employee, Assignment, Work
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'emp_address_temporary', 'emp_address_permanent', 'emp_date_of_birth', 'emp_national', 'emp_email', 'emp_contact_number','emp_image']
        labels = {
            'emp_id': 'AutoIncrement Number',
            'emp_name': 'Employee Full Name',
            'emp_address_temporary': 'Employee Temporary Address',
            'emp_address_permanent': 'Employee Permanent Address',
            'emp_date_of_birth': 'Employee Date of Birth',
            'emp_national': 'Employee Nationality',
            'emp_email': 'Employee Email',
            'emp_contact_number': 'Employee Contact Number',
            'emp_image':'Photo of Employee'
        }
        widgets={
            'emp_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_address_temporary': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_address_permanent': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'emp_national': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'emp_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['boss_name', 'emp_name', 'work_primary']
        labels = {
            'boss_name': 'Company Boss Name',
            'emp_name': 'Employee Name which one is assigned',
            'work_primary': 'Where is assigned to work'
        }
        widgets = {
            'boss_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_name': forms.Select(attrs={'class': 'form-control'}),
            'work_primary': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['emp_name'].queryset = Employee.objects.all()

        # Override label_from_instance method to display only the employee name
        self.fields['emp_name'].label_from_instance = lambda obj: "%s" % obj.emp_name

        self.fields['work_primary'].queryset = Work.objects.all()
        self.fields['work_primary'].label_from_instance = lambda obj: "%s" % obj.work_primary