from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient_list"),
    path("ingredients/<int:pk>", views.IngredientDetailView.as_view(), name="ingredient_detail"),
    path("ingredients/new", views.IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredients/update/<int:pk>", views.IngredientUpdateView.as_view(),
         name="ingredient_update"),
    path("ingredients/delete/<int:pk>", views.IngredientDeleteView.as_view(),
         name="ingredient_delete"),
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/new", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<int:pk>", views.RecipeDetailView.as_view(),
         name="recipe_detail"),
    path("recipes/update/<int:pk>", views.RecipeUpdateView.as_view(),
         name="recipe_update"),
    path("recipes/delete/<int:pk>", views.RecipeDeleteView.as_view(),
         name="recipe_delete"),
]