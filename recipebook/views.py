from django.shortcuts import render, get_object_or_404
from .models import Cuisine, Meal, Recipe
from django.http import HttpResponse
from django.views import generic, View


# def display_recipe(request):

#     return render(request, 'recipe.html')

class RecipeCollection(generic.ListView):
    queryset = Recipe.objects.values_list('title')
    template_name = 'recipe.html'
    paginate_by = 9
