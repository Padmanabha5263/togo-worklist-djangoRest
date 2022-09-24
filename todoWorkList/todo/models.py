from django.db import models

# Create your models here.

class Superiors(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    doj = models.DateField()
    address =models.CharField(max_length=50)
    class Meta:
        db_table="todo_Superiors"

    def __str__(self):
        return f'name = {self.name} , email = {self.email}'

class Employees(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    doj = models.DateField()
    address =models.CharField(max_length=50)
    SupervisorId = models.ForeignKey(Superiors, on_delete=models.CASCADE)
    class Meta:
        db_table="todo_Employees"

    def __str__(self):
        return f'name = {self.name} , email = {self.email}'

class Worklist(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    enddate = models.DateField()
    isWorkDone = models.BooleanField(default=False)
    empId = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='worklists')
    class Meta:
        db_table="todo_Worklist"

    def __str__(self):
        return f'name = {self.name} '

