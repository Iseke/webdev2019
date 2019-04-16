from rest_framework import serializers
from api.models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'
        read_only_fields = ['id']


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)
    status = serializers.CharField(default='NS')
    task_list = TaskListSerializer(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
