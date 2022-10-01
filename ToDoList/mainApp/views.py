from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics 
from rest_framework.permissions import BasePermission,IsAuthenticated,IsAdminUser
from .serializers import *
from .models import *
from .permissions import * 



class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = [IsOwnerOrReadOnly] 
    

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
   


class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    
    

    
class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]