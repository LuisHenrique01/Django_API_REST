from .models import Todo, Produtos
from rest_framework import serializers

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'create_add']
        

class ProdutoSerializes(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'qtd_estoque']