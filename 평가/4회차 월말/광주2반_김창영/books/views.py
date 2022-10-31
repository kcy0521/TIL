from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':
        books = get_object_or_404(Book)
        serializer = BookListSerializer(many=True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':
        serializer = BookSerializer(request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    books = get_object_or_404(Book)
    if request.method == 'GET':
        serializer = BookSerializer(many=True)
        return Response(serializer.data)
    # Q 4.
    elif request.method == 'DELETE':
        request.delete()
        data = {
            'dalete' : f'{book_pk}번이 삭제되었습니다.'
        }
        return Response(data, selializer.data)
    # Q 5.
    elif request.mehtod == 'PUT':
        pass


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    comments = get_object_or_404(Comment)
    serializer = CommentSerializer(many=True) 
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    serializer = CommentSerializer(many=True)
    if request.is_valid(raise_exceptions=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    comments = get_object_or_404(Comment)
    # Q 9.
    if request.method == 'GET':
        serializer = CommentSerializer(many=True)
        return Response(serializer.data)
    # Q 10.
    elif request.method == 'DELETE':
        request.delete()
        data = {
            'dalete' : f'{comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, selializer.data)

