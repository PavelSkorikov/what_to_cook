from django.contrib import admin
from main_app.models import *

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """форма рецепта"""
    list_display = ('title',
                    'description',
                    'image',
                    'dish',
                    'ingredients',
                    'steps',
                    'procedure',
                    'createAt',
                    'user',
                    'cooking_time',
                    'servings',
                    'likes',
                    'dislikes',
                    'complexity',
                    )
    list_display_links = ('title',)
    list_filter = ('title', 'user', 'createAt', 'cooking_time', 'dish', 'likes', 'dislikes', 'complexity',)

@admin.register(Ingridient)
class IngridientAdmin(admin.ModelAdmin):
    """форма ингидиента"""
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(Steps)
class StepsAdmin(admin.ModelAdmin):
    """форма этапа приготовления"""
    list_display = ('number', 'image', 'action')
    list_display_links = ('number',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """коментарий"""
    list_display = ('comment', 'user', 'recipe', 'createAt')
    list_display_links = ('comment', 'recipe', 'user')
    list_filter = ('user', 'recipe', 'createAt')
