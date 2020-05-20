from .views import todo_list, todo_put_delete, ProdutosTodos, ProdutosDetalhado
from django.urls import path

urlpatterns = [
    path('api/todo/', todo_list),
    path('api/todo/<int:pk>/', todo_put_delete),
    path('api/prod/', ProdutosTodos.as_view()),
    path('api/prod/<int:pk>/', ProdutosDetalhado.as_view())
]