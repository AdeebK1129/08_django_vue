import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.forms.models import model_to_dict

from .models import Ingredient, Recipe
from .forms import RecipeForm

# Views

## Ingredients

class IngredientListView(ListView):
    model = Ingredient


class IngredientDetailView(DetailView):
    model = Ingredient

class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ["name"]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Ingredient "{ingredient_name}" has been created'.format(
                ingredient_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("recipes:ingredient_detail", args=[self.object.id])

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ["name"]
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Ingredient "{ingredient_name}" has been updated'.format(
                ingredient_name=self.object.name))
        return response
    
    def get_success_url(self):
        return reverse_lazy("recipes:ingredient_detail", args=[self.object.id])
    
class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy("recipes:ingredient_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Ingredient "{ingredient_name}" has been deleted'.format(
                ingredient_name=self.object.name))
        return response


# Recipes

class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    # form_class = RecipeForm
    fields = ["name", "ingredients", "foodDescription", "recipe" ]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Recipe "{recipe_name}" has been created'.format(
                recipe_name=self.object.name))
        return response
    
    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("recipes:recipe_detail", args=[self.object.id])
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       ingredient_list = list(Ingredient.objects.all().values())
       context["ingredient_list"] = ingredient_list
       context["ingredient_list"] = json.dumps(ingredient_list)
       print("context", context)
       return context

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name_suffix = '_edit'
    fields = ["name", "ingredients", "foodDescription", "recipe" ]
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Recipe "{recipe_name}" has been updated'.format(
                recipe_name=self.object.name))
        return response
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       recipe_dico = model_to_dict(self.object)
       ingredients = recipe_dico["ingredients"]
       recipe_ingredient_list = []
       for ingredient in ingredients:
           recipe_ingredient_list.append({"id": ingredient.id, "name": ingredient.name})
       recipe_dico["ingredients"] = json.dumps(recipe_ingredient_list)
       ingredient_list = list(Ingredient.objects.all().values())
       context["recipe_dict"] = json.dumps(recipe_dico)
       context["ingredient_list"] = json.dumps(ingredient_list)
       print("context", context)
       return context
    
    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("recipes:recipe_detail", args=[self.object.id])

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes:recipe_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Recipe "{recipe_name}" has been deleted'.format(
                recipe_name=self.object.name))
        return response
    
class RecipeUpdatebisView(View):
    def post(self, request, *args, **kwargs):
       recipe = get_object_or_404(Recipe, pk=self.kwargs["pk"])
       # Create a form instance with POST data
       form = RecipeForm(request.POST, instance=recipe)
       if form.is_valid():
           form.save()
           return JsonResponse({"success": True})
       else:
           return JsonResponse({"success": False, "errors": form.errors})
    
class RecipeDetailbisView(TemplateView):
    template_name = "recipes/recipe_detailbis.html"
    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = self.kwargs["pk"]
        return context
    
class RecipeDetailJsView(View):
    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=self.kwargs["pk"])
        recipe_js = model_to_dict(recipe)
        recipe_js["ingredients"] = []
        for ingredient in recipe.ingredients.values():
            recipe_js["ingredients"].append(ingredient)
        return JsonResponse({"recipe": recipe_js})

