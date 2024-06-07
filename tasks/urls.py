from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/update_status/', views.update_task_status, name='update_task_status'),  # Adicionar URL para atualizar o status
    path('report/', views.task_report, name='task_report'),  # Adicionar URL para o relatório
    path('category/create/', views.category_create, name='category_create'),  # Adicionar URL para criar categoria
]
