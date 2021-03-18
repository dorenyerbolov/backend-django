from rest_framework import serializers

from main.models import TodoList, TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'


class TodoRetrieveSerializer(serializers.ModelSerializer):
    todo_items = TodoItemSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'todo_items')


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
