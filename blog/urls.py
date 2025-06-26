from django.urls import path
from .views import *



urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('posts/', BlogPostView.as_view()),   
    path('posts/<int:pk>/', BlogPostIDView.as_view()),
]