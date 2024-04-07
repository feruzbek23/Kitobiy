from account.serializers import UserResgistrationSerializer 
from .models import UserProfile
from rest_framework import viewsets
from . import permissions

class UserRegisterView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserResgistrationSerializer
    permission_classes = (permissions.UpdateProfile,)



