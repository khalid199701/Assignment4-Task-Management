from django.db import models
from taskModel.models import TaskModel
# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length= 100)
    task = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.category_name

