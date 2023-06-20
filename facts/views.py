from .models import AnimalFact, CapitalFact
from .serializers import AnimalSerializers, CapitalSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random
from django.shortcuts import render

def home(response):
    return render(response, "facts/home.html")

@api_view(['GET', 'POST'])
def fun_animal_facts(request):
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
def fun_capital_facts(request):
    if request.method == "GET":
        facts = CapitalFact.objects.all()
        fact = random.choice(facts)
        serializer = CapitalSerializers(fact)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CapitalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)