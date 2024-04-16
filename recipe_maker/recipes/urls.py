from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<int:pk>", views.RecipeDetailView.as_view(),
        name="recipe_detail"),
    path("recipes/new", views.RecipeCreateView.as_view(), name="recipe_create"),
]