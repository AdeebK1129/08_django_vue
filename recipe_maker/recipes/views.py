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