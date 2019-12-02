from rest_framework import serializers
from . models import application
from . models import apikey

class applicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = application
        fields = ('id','title')

class apikeySerializer(serializers.ModelSerializer):

    class Meta:
        model = apikey
        fields = ('id','key')
