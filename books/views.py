from django.shortcuts import render

from books.models import Books
from books.serializers import BooksSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BooksList(APIView):
    """
    List all books, or create a new books.
    """
    def get(self, request, format=None):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksDetail(APIView):
    """
    Retrieve, update or delete a books instance.
    """
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        books = self.get_object(pk)
        serializer = BooksSerializer(books)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_object(pk)
        serializer = BooksSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        books = self.get_object(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

