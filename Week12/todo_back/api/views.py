from django.shortcuts import render
from api.models import TaskList, Task
from django.http import JsonResponse
from api.serializers import TaskListSerializer, TaskSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer(data=body)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_details(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=body)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({}, status=204)

    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskSerializer(data=body)

        if serializer.is_valid():
            serializer.save(task_list=task_list)

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

    return JsonResponse({'error': 'bad request'})
