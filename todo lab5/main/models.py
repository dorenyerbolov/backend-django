from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Туду лист'
        verbose_name_plural = 'Туду листы'

    def __str__(self):
        return f"{self.name}"


class TodoItem(models.Model):
    MARK = [
        ('D', 'Done'),
        ('ND', 'Not Done')
    ]
    title = models.CharField(max_length=255, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    due_on = models.DateTimeField(verbose_name='Дата и время дедлайна')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    mark = models.CharField(max_length=2, choices=MARK, verbose_name='Статус')
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todo_items', verbose_name='Туду лист')

    class Meta:
        verbose_name = 'Тудушка'
        verbose_name_plural = 'Тудушки'

    def __str__(self):
        return f"{self.title}"
