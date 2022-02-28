from rest_framework import serializers
from books.models import Books
from django.contrib.auth.models import User

class BooksSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Books
        fields = ['id', 'bookname','bookauthor', 'booklan', 'owner']


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Books.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'books']