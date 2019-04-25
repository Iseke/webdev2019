from django.contrib import admin
from api.models import TaskList,Task
# Register your models here.

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_by')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','due_on','status','task_list')