from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author', 'excerpt', 'content', 'status') #jakie dane z modelu chcemy convertować, żeby front-end miał wygodnie :P