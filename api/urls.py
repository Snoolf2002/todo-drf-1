from django.urls import path
from .views import TodoApiView

urlpatterns = [
    path('todos/', TodoApiView.as_view())
]