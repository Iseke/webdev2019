from django.urls import path
from api import views
urlpatterns=[
    path('task_lists/',views.TaskLists.as_view()),
    path('task_lists/<int:pk>/',views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.TaskListTasks.as_view()),
    # path('task_lists/<int:pk>/tasks/', views.task_list_details),

    #path('user/',views.UserList.as_view()),
#     path('login/', views.login),
#     path('logout/', views.logout),
#
]