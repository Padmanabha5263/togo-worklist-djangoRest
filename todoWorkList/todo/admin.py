from django.contrib import admin
from todo.models import Worklist, Employees, Superiors

# Register your models here.
admin.site.register(Worklist)
admin.site.register(Employees)
admin.site.register(Superiors)