from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class RecipeListView(APIView):
    # вывод списка рецептов
    def get(self, request):
        recipes = Recipe.objects
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data)

