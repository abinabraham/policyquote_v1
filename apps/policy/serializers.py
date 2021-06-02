from apps.policy.models import Quote, Policy, PolicyType, AgeBand
from rest_framework import serializers
from apps.accounts.serializers import UserSerializer
from apps.accounts.models import User

class AgeBandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgeBand
        fields = ('id', 'url', 'age_from', 'age_to',)

class PolicyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PolicyType
        fields = ('id', 'url', 'type_name', 'is_active',)

class PolicySerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.PrimaryKeyRelatedField(
        queryset=PolicyType.objects.all()
    )
    age_band = serializers.PrimaryKeyRelatedField(
        queryset=AgeBand.objects.all()
    )
    class Meta:
        model = Policy
        fields = ('id', 'url', 'types', 'premium','cover','age_band',)

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('quote', 'customer','types','status',)


