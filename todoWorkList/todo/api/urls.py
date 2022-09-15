from django.urls import path
from . import views

urlpatterns = [
    path('works/', views.todoWorks, name="add work"),
    path('works/<int:pk>', views.todoWork, name="add work list"),
]