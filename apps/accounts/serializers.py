from apps.accounts.models import User
from rest_framework import serializers
import string    
import random # define the random module  
import datetime


class UserSerializer(serializers.HyperlinkedModelSerializer):
    dob = serializers.DateField(format="%d-%m-%Y",input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'dob', 'username')
