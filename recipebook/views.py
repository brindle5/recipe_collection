from django.shortcuts import render, get_object_or_404
from .models import Cuisine, Meal, Recipe
from django.http import HttpResponse
from django.views import generic, View


# def display_recipe(request):

#     return render(request, 'recipe.html')

class RecipeCollection(generic.ListView):
    template_name = 'recipe.html'
    model = Recipe


# class RecipeCollection(View):
#     def get(self, request, *args, **kwargs):
#         queryset = Recipe.objects.all()
#         context = {"recipes": queryset}
#         return render(request, 'recipe.html', context)


# def recipe_collection(request):
#     recipes = Recipe.objects.all()
#     context = {"recipes": recipes}
#     return render(request, 'recipe.html', context)
