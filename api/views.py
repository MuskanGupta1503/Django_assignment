from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import status

@api_view(['POST'])
def create_blogpost(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': "Data Created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_blogpost(request, pk):
    id = pk
    stu = BlogPost.objects.get(pk=id)
    serializer = BlogPostSerializer(stu, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': "Complete Data Updated"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_blogposts(request):
    stu = BlogPost.objects.all()
    serializer = BlogPostSerializer(stu, many=True)
    return Response(serializer.data)
