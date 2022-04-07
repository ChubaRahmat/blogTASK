from django.shortcuts import render

from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from posts.serializers import PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer





    def get_serializer_context(self):
        return {'request': self.request}