from rest_framework import viewsets
from rest_framework import permissions
from apps.accounts.serializers import UserSerializer
from rest_framework import generics
from apps.accounts.models import User
from datetime import datetime
from uuid import uuid4

from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

