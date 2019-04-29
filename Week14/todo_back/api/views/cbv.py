from api.models import TaskList,Task
from rest_framework.response import Response
from django.http import Http404
from api.serializers import TaskListSerializer,TaskSerializer
from rest_framework import status
from rest_framework.views import APIView


class TaskLists(APIView):
    def get(self,request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class TaskListDetail(APIView):
    def get_objects(self,pk):
        try:
            return  TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        task_list = self.get_objects(pk)
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        task_list= self.get_objects(pk)
        serializer = TaskListSerializer(instance=task_list,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,pk):
        task_list = self.get_objects(pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListTasks(APIView):
    def get_objects(self,pk):
        try:
            return  TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        task_list = self.get_objects(pk)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,pk):
        task_list = self.get_objects(pk)
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(task_list=task_list)
        return Response(serializer.data,status=status.HTTP_200_OK)
