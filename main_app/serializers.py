from rest_framework import serializers
from main_app.models import *

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'image', 'user', 'createAt')



