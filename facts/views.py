from .models import AnimalFact, CapitalFact
from .serializers import AnimalSerializers, CapitalSerializers
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render
from django.http import HttpResponseBadRequest
import random
import json

def home(response):
    return render(response, "facts/home.html")

class AnimalList(generics.ListCreateAPIView):
    queryset = AnimalFact.objects.all()
    serializer_class = AnimalSerializers

    def list(self, request):
        queryset = self.get_queryset()
        query = random.choice(queryset)
        serializer = AnimalSerializers(query)
        return Response(serializer.data)

class CapitalList(generics.ListCreateAPIView):
    queryset = CapitalFact.objects.all()
    serializer_class = CapitalSerializers

    def list(self, request):
        queryset = self.get_queryset()
        query = random.choice(queryset)
        serializer = CapitalSerializers(query)
        return Response(serializer.data)

    def create(self, request):
        serializer = CapitalSerializers(data=self.request.data)
        if serializer.is_valid():
            if check_fact(serializer):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return HttpResponseBadRequest('Invalid input', status=405)
            
def check_fact(serializer):
    file = open('facts/states.json')
    check = json.load(file)

    if check.get(serializer.validated_data["state"].title(), "N/A") != "N/A":
        if check[serializer.validated_data["state"].title()]["capital"]== serializer.validated_data["name"].title():
            return True
    return False