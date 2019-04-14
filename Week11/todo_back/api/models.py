from django.db import models
from datetime import datetime, timedelta
class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}: {self.name}'
    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=(datetime.now() + timedelta(days=10)))
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'task_list':self.task_list.name
        }
