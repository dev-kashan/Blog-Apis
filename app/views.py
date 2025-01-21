from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *

class BlogsApi(APIView):
    def get(self , request):
        blogs = Blog.objects.all().order_by('-id')
        serializer = BlogSerializer(blogs , many=True)
        return Response({"data": serializer.data})

class RecentBlogsApi(APIView):
    def get(self , request):
        recent_blogs = Blog.objects.all().order_by('-id')[:3]
        recent_serializer = BlogSerializer(recent_blogs , many=True)
        return Response({'data':recent_serializer.data})

class CategoryApi(APIView):
    def get(self , request):
        category = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(category , many=True)
        return Response({"data": serializer.data})

class BlogDetailApi(APIView):
    def get(self , request , id):
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(blog)
        return Response({"data": serializer.data})

class CategoryBlogApi(APIView):
    def get(self , request , id):
        blog = Blog.objects.filter(category__id=id)
        serializer = BlogSerializer(blog , many=True)
        return Response({"data": serializer.data})

# Create your views here.
