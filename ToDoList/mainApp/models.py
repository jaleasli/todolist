from django.db import models
from user.models import User
# Create your models here.

class ToDo(models.Model):
  user = models.ForeignKey(
    User, on_delete=models.CASCADE, null=True, blank=True)

  title = models.CharField(max_length=100, blank=False)
  description = models.TextField(blank=True)
  date = models.DateField(blank=False)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title 