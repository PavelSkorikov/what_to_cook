from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *

class RecipeListView(generics.ListAPIView):
    serializer_class = RecipeListSerializer
    permission_classes = (AllowAny, )
    def get_queryset(self):
        return Recipe.objects.order_by('-createAt')

class RecipeDetailView(generics.RetrieveAPIView):
    serializer_class = RecipeDetailSerializer
    permission_classes = (AllowAny, )
    queryset = Recipe.objects.all()

class IngridientListView(generics.ListAPIView):
    serializer_class = IngridientListSerializer
    permission_classes = (AllowAny, )
    def get_queryset(self):
        return Ingridient.objects.order_by('name')
