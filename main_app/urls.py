from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('recipe/all/', views.RecipeListView.as_view()),
    path('recipe/detail/<uuid:pk>', views.RecipeDetailView.as_view()),
    path('ingredient/all/', views.IngridientListView.as_view()),
]
