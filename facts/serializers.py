from rest_framework import serializers
from .models import AnimalFact, CapitalFact

class AnimalSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimalFact
        fields = ['info']

class CapitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = CapitalFact
        fields = ['info']