from rest_framework import serializers
from api.models import TaskList, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = TaskList
        fields = ('id','name','created_by',)


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)
    status = serializers.CharField(default='NS')
    task_list = TaskListSerializer(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

