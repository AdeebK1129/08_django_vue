from os import path
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

## Recipes

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

    def get_success_url(self):
        return reverse_lazy("recipes:recipe_detail", args=[self.object.id])

class RecipeUpdatebisView(View):
   def post(self, request, *args, **kwargs):
       movie = get_object_or_404(Recipe, pk=self.kwargs["pk"])
       # Create a form instance with POST data
       form = RecipeForm(request.POST, instance=movie)
       if form.is_valid():
           form.save()
           return JsonResponse({"success": True})
       else:
           return JsonResponse({"success": False, "errors": form.errors})

class RecipeDetailbisView(TemplateView):
    template_name = "recipes/recipe_detailbis.html"
    
    def get(self, request, *args, **kwargs):
        movie = get_object_or_404(Recipe, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_id'] = self.kwargs["pk"]
        return context