from api.models import TaskList,Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import TaskListSerializer,TaskSerializer
from rest_framework import status


@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def task_list_details(request,pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def task_list_tasks(request,pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(task_list=task_list)
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'error': 'bad request'})

