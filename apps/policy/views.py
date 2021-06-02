from rest_framework import viewsets
from rest_framework import permissions
from apps.policy.serializers import QuoteSerializer, PolicySerializer, PolicyTypeSerializer \
                                    , AgeBandSerializer
from rest_framework import generics
from apps.policy.models import Quote, Policy, PolicyType, AgeBand

from rest_framework.response import Response
from rest_framework.views import APIView


class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class PolicyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated]

class PolicyTypeviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PolicyType.objects.all()
    serializer_class = PolicyTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgeBandviewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AgeBand.objects.all()
    serializer_class = AgeBandSerializer
    permission_classes = [permissions.IsAuthenticated]


