from django.contrib import admin
from main_app.models import *

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """форма рецепта"""
    list_display = ('title', 'description', 'image', 'steps', 'createAt', 'user')
    list_display_links = ('title',)

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
