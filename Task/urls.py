from django.urls import path
from . import views

urlpatterns = [
    #index 
     path('', views.index),
    # Auth
    path('auth/register/', views.RegisterView.as_view()),
    path('auth/login/',    views.LoginView.as_view()),
    path('auth/logout/',   views.LogoutView.as_view()),

    # Tasks
    path('tasks/',          views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),

    # Subtasks
    path('tasks/<int:task_pk>/subtasks/',          views.SubtaskListCreateView.as_view()),
    path('tasks/<int:task_pk>/subtasks/<int:pk>/', views.SubtaskDetailView.as_view()),
]