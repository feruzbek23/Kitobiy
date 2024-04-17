from rest_framework import serializers
from .models import AuthorModel, BookModel

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id','name')

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    book_file = serializers.FileField()
    class Meta:
        model = BookModel
        author = AuthorSerializer(serializers.IntegerField)

        status = serializers.ChoiceField(choices=BookModel.STATUS)
        fields = (
            "id",
            "title",
            "author",
            "created_at",
            "status",
            "book_file",
        )
        


    
# Serializer for book file
class FileUploadSerializer(serializers.Serializer):
    book_file = serializers.FileField()
