from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        created_at = serializers.DateTimeField(format='%d/%m/%y/ %h:%m:%s', read_only=True)
        fields = ('id', 'title', 'category', 'author', 'created_at', 'text')
