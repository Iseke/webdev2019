from django.db import models
from datetime import timedelta, datetime


# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    TASK_CHOICES = (
        ('NS', 'Not Started'),
        ('IP', 'In Progress'),
        ('D', 'Done')
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=(datetime.now() + timedelta(days=7)))
    status = models.CharField(max_length=255, choices=TASK_CHOICES)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'task_list_name': self.task_list.name
        }
