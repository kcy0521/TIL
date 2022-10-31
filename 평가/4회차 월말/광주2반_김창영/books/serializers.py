from rest_framework import serializers
from .models import Book, Comment


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):
    # Q 6.
    class Meta:
        model = Comment
        fields = ('id','content','created_at','updated_at')


class BookSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # Q 11.
    

    class Meta:
        model = Book
        fields = '__all__'
