from .models import AnimalFact, CapitalFact
from .serializers import AnimalSerializers, CapitalSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponseBadRequest
import random
import json

def home(response):
    return render(response, "facts/home.html")

@api_view(['GET', 'POST'])
def fun_animal_facts(request, format=None):
    if request.method == "GET":
        facts = AnimalFact.objects.all()
        fact = random.choice(facts)
        serializer = AnimalSerializers(fact)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = AnimalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def fun_capital_facts(request, format=None):
    if request.method == "GET":
        facts = CapitalFact.objects.all()
        fact = random.choice(facts)
        serializer = CapitalSerializers(fact)
        return Response(serializer.data)
    if request.method == "POST":
        request.data["name"] = request.data["name"].title()
        request.data["state"] = request.data["state"].title()
        serializer = CapitalSerializers(data=request.data)

        if serializer.is_valid():
            if check_fact(serializer=serializer):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return HttpResponseBadRequest('Invalid input', status=405)

def check_fact(serializer):
    file = open('facts/states.json')
    check = json.load(file)

    if check.get(serializer.validated_data["state"], "N/A") != "N/A":
        if check[serializer.validated_data["state"]]["capital"] == serializer.validated_data["name"]:
            return True
    return False