from rest_framework import serializers
from account.models import UserModel
from django.contrib.auth.hashers import make_password

class UserResgistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "email",  
            "password",
        )
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def create(self, validated_data):
        return UserModel.objects.create(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=make_password(validated_data['password']))