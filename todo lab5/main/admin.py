from django.contrib import admin

# Register your models here.
from main.models import TodoItem, TodoList

admin.site.register(TodoItem)
admin.site.register(TodoList)