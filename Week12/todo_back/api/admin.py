from django.contrib import admin
from api.models import TaskList, Task


# Register your models here.

class TaskListAdmin(admin.ModelAdmin):
    search_fields = ['name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'task_list']


admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)
