from rest_framework import serializers
from .models import Author, BlogPost

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at']