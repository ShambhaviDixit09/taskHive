from django.db import models
from django.contrib.auth.models import User

class AddNewTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, blank = True)
    task_title = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=1000)
    date_to_comp = models.DateField()

    def __str__(self):
        return self.task_title
