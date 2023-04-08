from django.urls import path
from .views import TodoApiView, update_task, delete_task

urlpatterns = [
    path('todos/', TodoApiView.as_view()),
    path('todos/<int:id>/', update_task),
    path('todos/<int:id>/delete/', delete_task)
]