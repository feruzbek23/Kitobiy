from rest_framework import serializers
from .models import UserProfile


class UserResgistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "username",
            "email",  
            "password",
        )
        extra_kwargs = {
            'password': {'write_only':True}
        }