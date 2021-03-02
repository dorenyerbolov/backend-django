from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class TodoItem(models.Model):
    MARK = [
        ('D', 'Done'),
        ('ND', 'Not Done')
    ]
    title = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=datetime.now() + timedelta(days=2))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(max_length=2, choices=MARK)

    class Meta:
        verbose_name = 'Тудушка'
        verbose_name_plural = 'Тудушки'

    def __str__(self):
        return f"{self.title}"
