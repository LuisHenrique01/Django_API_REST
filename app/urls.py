from .views import todo_list, todo_put_delete
from django.urls import path

urlpatterns = [
    path('', todo_list),
    path('<int:pk>', todo_put_delete),
]