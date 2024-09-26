from rest_framework import serializers
from .models import AuthorModel, BookModel

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id','name')

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookModel
        author = AuthorSerializer(serializers.IntegerField)
        rate_stars = serializers.ChoiceField(choices=BookModel.STARS)
        status = serializers.ChoiceField(choices=BookModel.STATUS)
        fields = (
            "id",
            "title",
            "author",
            "created_at",
            "status",
            "rate_stars",
            "user",
            
            
        )
        


    
