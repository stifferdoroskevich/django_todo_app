from django.urls import path
from .views import TaskCreate, TaskDetail, TaskList, TaskUpdate, TaskDelete


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task/', TaskCreate.as_view(), name='create_task'),
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
]
