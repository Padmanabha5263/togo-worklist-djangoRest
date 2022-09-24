from rest_framework import serializers
from todo.models import Worklist, Employees, Superiors

class WorklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklist
        fields = '__all__'


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superiors
        fields = '__all__'

class EmployeelistSerializer(serializers.ModelSerializer):
    worklists = WorklistSerializer(many=True, read_only=True)
    class Meta:
        model = Employees
        fields = '__all__'

