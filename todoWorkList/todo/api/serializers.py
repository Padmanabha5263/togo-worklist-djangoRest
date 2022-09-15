from rest_framework import serializers
from todo.models import Worklist

class WorklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklist
        fields = '__all__'