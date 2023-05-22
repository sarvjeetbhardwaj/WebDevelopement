from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('', views.TaskList, name='tasks'),
    path('task/<str:pk>', views.TaskDetail, name='task_detail'),
    path('task_create/', views.TaskCreate, name='task_create'),
    path('task_update/<str:pk>', views.TaskUpdate, name='task_update'),
    path('task_delete/<str:pk>', views.TaskDelete, name='task_delete'),
    path('delete_confirmation/<str:pk>', views.DeleteConfirmation, name='task_delete_confirmation'),
]