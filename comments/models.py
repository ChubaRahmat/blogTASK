from django.db import models

from account.models import User


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.text

