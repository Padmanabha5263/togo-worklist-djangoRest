from django.db import models

# Create your models here.

class Worklist(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    enddate = models.DateField()
    email = models.EmailField()
    isWorkDone = models.BooleanField(default=False)

    class Meta:
        db_table="todo_Worklist"

    def __str__(self):
        return f'name = {self.name} , emial = {self.email}'