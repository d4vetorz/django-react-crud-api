from rest_framework import serializers
from .models import Task


# esta funcion convierte los tipos de datos de pyton a Json
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'title', 'description', 'done')
        fields = '__all__'