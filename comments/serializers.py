from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        created_at = serializers.DateTimeField(format='%d/%m/%y/ %h:%m:%s', read_only=True)
        fields = ('author', 'created_at', 'text')
