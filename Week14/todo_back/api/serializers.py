from rest_framework import serializers
from api.models import TaskList, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)
    status = serializers.CharField(default='NS')
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id','name','created_at','due_on','status','task_list_id')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)
    status = serializers.CharField(default='NS')


    class Meta:
        model = Task
        fields = ('id','name','created_at','due_on','status')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    tasks = TaskSerializer2(many=True)

    class Meta:
        model = TaskList
        fields = ('id','name','created_by', 'tasks')

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        task_list = TaskList.objects.create(**validated_data)
        # for task in tasks:
        #     Task.objects.create(task_list=task_list,**task)
        arr=[Task(task_list=task_list, **task) for task in  tasks]
        Task.objects.bulk_create(arr)
        return task_list


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    # tasks = serializers.StringRelatedField(many=True)
    tasks = TaskSerializer(many=True)
    # tasks = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = TaskList
        fields = ('id','name','created_by', 'tasks')
