from api.models import TaskList,Task
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from api.serializers import TaskListSerializer,TaskSerializer,UserSerializer,TaskListSerializer2,TaskSerializer2
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.filters import TaskFilter
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class TaskLists(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer2
    def get_queryset(self):
        return TaskList.objects.filter(created_by = self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)



class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListTasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter , filters.OrderingFilter)
    # TODO DjangoFilterBackend
    filter_class = TaskFilter
    # filterset_fields = ('name', 'status')

    # TODO SearchFilter
    search_fields  = ('status',)

    # TODO OrgeringFilter
    ordering_fields = ('name', )
    ordering = ('id')

    def get_queryset(self):
        try:
            task_list= TaskList.objects.get(id=self.kwargs.get('pk'))
        except TaskList.DoesNotExist:
            raise Http404

        queryset = task_list.tasks.all()

        # name = self.request.query_params.get('name',None)
        # status = self.request.query_params.get('status', None)
        # if name is not None and status is not None:
        #     queryset = queryset.filter(name=name).filter(status=status)

        return queryset

