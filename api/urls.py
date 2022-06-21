from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='api-view'),
    path('list/', views.taskList, name='task-list'),
    path('detail/<int:pk>/', views.taskDetail, name='task-detail'),
    path('create/', views.taskCreate, name='task-create'),
    path('update/<int:pk>/', views.taskUpdate, name='task-update'),
    path('delete/<int:pk>/', views.taskDelete, name='task-delete'),
    path('login', views.login_api, name='login'),
    path('register', views.register_api, name='register'),
]