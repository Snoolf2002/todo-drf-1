from django.urls import path
from .views import TodoApiView, update_task, delete_task, UserView

urlpatterns = [
    path('todos/', TodoApiView.as_view()),
    path('todos/<int:id>/', TodoApiView.as_view()),
    path('todos/<int:id>/update/', update_task),
    path('todos/<int:id>/delete/', delete_task),
    path('user/<str:user>/', UserView.as_view()),
]