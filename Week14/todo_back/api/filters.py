from django_filters import rest_framework as filters
from api.models import Task

class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    min_date = filters.DateTimeFilter(field_name='created_at',lookup_expr='gte')
    max_date = filters.DateTimeFilter(field_name='created_at',lookup_expr='lte')
    status = filters.CharFilter(lookup_expr='exact')
    class Meta:
        model= Task
        fields = ('name','created_at','status' )
