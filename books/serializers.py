from rest_framework import serializers
from books.models import Books
from django.contrib.auth.models import User


class BooksSerializer(serializers.ModelSerializer):
    # books = serializers.PrimaryKeyRelatedField(many=True, queryset=Snips.objects.all())
    class Meta:
        model = Books
        fields = ['id', 'bookname','bookauthor', 'booklan']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']