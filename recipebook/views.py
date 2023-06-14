from django.shortcuts import render, redirect, get_object_or_404
from .models import Cuisine, Meal, Recipe
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from .forms import RecipeForm
from django.urls import reverse


class RecipeCollection(generic.ListView):
    template_name = 'index.html'
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


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe")
    form = RecipeForm()
    context = {
        'form': form
    }
    return render(request, 'add_recipe.html', context)


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe")
    form = RecipeForm(instance=recipe)
    context = {
        'form': form
    }
    return render(request, 'edit_recipe.html', context)


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect("recipe")
