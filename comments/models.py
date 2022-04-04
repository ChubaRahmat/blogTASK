from django.db import models

from account.models import MyUser


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.text

