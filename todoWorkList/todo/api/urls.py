from django.urls import path
from . import views

urlpatterns = [
    path('works/', views.todoWorks, name="works"),
    path('works/<int:pk>', views.todoWork, name="work"),
    path('employees/', views.todoEmployees, name="employees"),
    path('employees/<int:pk>', views.todoEmployee, name="employee"),
    path('supervisors/', views.todoSupervisors, name="supervisors"),
    path('supervisors/<int:pk>', views.todoSupervisor, name="supervisor")
]