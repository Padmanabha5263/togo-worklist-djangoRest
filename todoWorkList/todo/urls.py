from django.urls import path
from . import views

app_name='todoWork'
urlpatterns = [
    path('',views.home, name="homepage"),
    path('delete/',views.deleteTask, name="deleteTask")
]