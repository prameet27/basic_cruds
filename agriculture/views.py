from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Employee, Work, Assignment
from .forms import EmployeeForm, AssignmentForm

# Create your views here.

def index(request):
    return render(request, 'agriculture/index.html')

def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'agriculture/employee/employee_list.html', {'employees': employee})

def employee_details(request, id):
    employee = Employee.objects.filter(id=id)
    return render(request, 'agriculture/employee/employee_details.html', {'employees': employee})

def work_list(request):
    work = Work.objects.all()
    return render(request, 'agriculture/work/work_list.html', {'Works': work})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            new_employee = form.save(commit=False)  # Create a new employee object but don't save it yet
            new_employee.emp_id = form.cleaned_data['emp_id']
            new_employee.emp_name = form.cleaned_data['emp_name']
            new_employee.emp_address_temporary = form.cleaned_data['emp_address_temporary']
            new_employee.emp_address_permanent = form.cleaned_data['emp_address_permanent']
            new_employee.emp_date_of_birth = form.cleaned_data['emp_date_of_birth']
            new_employee.emp_national = form.cleaned_data['emp_national']
            new_employee.emp_email = form.cleaned_data['emp_email']
            new_employee.emp_contact_number = form.cleaned_data['emp_contact_number']
            new_employee.emp_image = form.cleaned_data['emp_image']
            new_employee.save()  # Now save the new employee object
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'agriculture/employee/employee_add.html', {'form': form})

def employee_edit(request,id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk = id)
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
    return render(request, 'agriculture/employee/employee_edit.html', {'form': form})

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('index')

def work_assign(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            new_assign = form.save(commit=False)
            new_assign.boss_name = form.cleaned_data['boss_name']
            new_assign.emp_name = form.cleaned_data['emp_name']
            new_assign.work_primary = form.cleaned_data['work_primary']
            new_assign.save()
            return redirect('index')
    else:
        form = AssignmentForm()
    return render(request, 'agriculture/work/work_assign.html', {'form': form})

def work_assign_list(request):
    assign = Assignment.objects.all()
    return render(request, 'agriculture/work/work_assign_list.html', {'assignments': assign})
