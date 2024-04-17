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

class IngredientListView(LoginRequiredMixin, ListView):
    model = Recipe

class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['name']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Ingredient "{ingredient_name}" has been created'.format(
                ingredient_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("recipes:recipe_detail", args=[self.object.id])
    
class IngredientDetailView(DetailView):
    model = Ingredient

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['name']
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Ingredient "{ingredient_name}" has been updated'.format(
                ingredient_name=self.object.name))
        return response
    
    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("recipes:ingredient_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})
    

class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy("recipes:ingredient_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Ingredient "{ingredient_name}" has been deleted'.format(
                actor_name=self.object.name))
        return response
    

# Recipes 
    
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm

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
    # you can also use it this way with kwargs, just to let you know
    # but here we have only one argument, so no mistake can be done
    #return reverse_lazy("movies:actor_detail",
    #                    kwargs={'pk':self.object.id})

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Recipe "{self.object.name}" has been updated'
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_dico = model_to_dict(self.object)
        ingredients = recipe_dico["recipes"]
        recipe_ingredient_list = [{"id": recipe.id, "name": recipe.name} for recipe in recipes]
        recipe_dico["ingredients"] = recipe_ingredient_list
        ingredient_list = list(Ingredient.objects.all().values())
        context["recipe_dict"] = recipe_dico
        context["ingredient_list"] = ingredient_list
        print("context", context)
        return context

    def get_success_url(self):
        return reverse_lazy("recipes:recipe_detail", args=[self.object.id])
        # You can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        # return reverse_lazy("movies:actor_detail", kwargs={'pk': self.object.id})


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