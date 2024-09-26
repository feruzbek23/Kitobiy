from rest_framework.views import APIView

from rest_framework import status
from .serializers import BookSerializer, BookModel, AuthorModel, AuthorSerializer
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.

# User authentification

class BookApiView(APIView):

    
    def get(self, request, pk=None):
        if pk is not None:
            try: 
                book = BookModel.objects.get(pk=pk)
                serializer = BookSerializer(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except BookModel.DoesNotExist:
                return Response({"error" : "Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            book = BookModel.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):    
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk):
        book = BookModel.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk=None):
        if pk is not None:
            book = BookModel.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        




class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class AuthorView(generics.ListCreateAPIView):
    
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
