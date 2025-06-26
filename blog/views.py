from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.


class AuthorView(APIView):
    
    def get(self, request):

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=AuthorSerializer)
    def post(self, request):
        
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        
class BlogPostIDView(APIView):

    def get(self, request, pk):

        post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(post)

        return Response(serializer.data)
    
class BlogPostView(APIView):
    
    def get(self, request):
        
        posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BlogPostSerializer)
    def post(self, request):

        serializer = BlogPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=BlogPostSerializer)
    def put(self, request, pk):
        
        post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=BlogPostSerializer)
    def delete(self, request, pk):

        post = get_object_or_404(BlogPost, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



