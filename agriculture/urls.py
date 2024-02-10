from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_details/<int:id>', views.employee_details, name='employee_details'),
    path('employee_add/', views.employee_add, name='employee_add'),
    path('employee_edit/<int:id>', views.employee_edit, name='employee_edit'),
    path('employee_delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('work_list/', views.work_list, name='work_list'),
    path('work_assign/', views.work_assign, name='work_assign'),
    path('work_assign_list.html', views.work_assign_list, name = 'work_assign_list'),
]
