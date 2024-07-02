from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для списка задач
    # Отображает список всех задач, доступных в системе
    path('', views.task_list, name='task-list'),

    # Маршрут для создания новой задачи
    # Отображает форму для создания новой задачи
    path('create/', views.task_create, name='task-create'),

    # Маршрут для деталей задачи
    # Отображает детали конкретной задачи по её идентификатору (pk)
    path('<int:pk>/', views.task_detail, name='task-detail'),

    # Маршрут для обновления задачи
    # Отображает форму для изменения существующей задачи по её идентификатору (pk)
    path('<int:pk>/update/', views.task_update, name='task-update'),

    # Маршрут для удаления задачи
    # Удаляет существующую задачу по её идентификатору (pk)
    path('<int:pk>/delete/', views.task_delete, name='task-delete'),
]

# без комментариев полностью :

# urlpatterns = [
#     path('', views.task_list, name='task-list'),
#     path('task/<int:pk>/', views.task_detail, name='task-detail'),
#     path('task/create/', views.task_create, name='task-create'),
#     path('task/<int:pk>/update/', views.task_update, name='task-update'),
#     path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),
# ]
