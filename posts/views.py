from django.db.models import Q
from django.shortcuts import render

from rest_framework import generics, viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .models import Post
from posts.serializers import PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['title', 'text']
    ordering_fields = ['title']


    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        print(request.query_params)
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) |
                                   Q(text__icontains=q))

        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)





    def get_serializer_context(self):
        return {'request': self.request}