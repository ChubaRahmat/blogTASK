from django.shortcuts import render
from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer
from posts.serializers import PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {'request': self.request}
