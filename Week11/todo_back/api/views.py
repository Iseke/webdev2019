from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import TaskList, Task


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


def task_list(request):
    task_lists = TaskList.objects.all()
    json_task_lists = [c.to_json() for c in task_lists]
    return JsonResponse(json_task_lists, safe=False)


def get_task_list(request, pk):
    try:
        get_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(get_list.to_json(), safe=False)


def get_task_by_id(request, pk):
    try:
        get_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    tasks = get_list.task_set.all()
    json_task = [c.to_json() for c in tasks]
    return JsonResponse(json_task, safe=False)
