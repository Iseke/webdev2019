from api.models import TaskList,Task
from django.contrib.auth.models import User
from django.http import Http404
from api.serializers import TaskListSerializer,TaskSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class TaskLists(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer
    def get_queryset(self):
        return TaskList.objects.filter(created_by = self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)



class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListTasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list=TaskList.objects.get(id=self.kwargs[self.lookup_field]))
