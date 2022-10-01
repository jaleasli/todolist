from rest_framework import serializers
from .models import *
from mainApp.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('user','id', 'title', 'description', 'date', 'completed')
        
