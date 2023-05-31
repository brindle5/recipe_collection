from django.shortcuts import render
from .models import Cuisine, Meal, Recipe
from django.http import HttpResponse
from django.views import generic, View


def display_recipe(request):
    return render(request, 'recipe.html')
