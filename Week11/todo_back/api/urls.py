from django.urls import path
from api import views
urlpatterns=[
    path('', views.index),
    path('task_lists/',views.task_list),
    path('task_lists/<int:pk>/',views.get_task_list),
    path('task_lists/<int:pk>/tasks/', views.get_task_by_id),

]