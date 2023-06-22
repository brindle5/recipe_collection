from django.shortcuts import render, redirect, get_object_or_404
from .models import Cuisine, Meal, Recipe
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from .forms import RecipeForm
from django.urls import reverse
from django.contrib import messages


class RecipeCollection(generic.ListView):
    template_name = 'index.html'
    model = Recipe

#  Views for adding, editing and deleting recipes taken from the Code Institute ToDo App project  # noqa


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Recipe has been added to recipebook')
            return redirect("recipe")
            messages.error(request, 'There was a problem. Try again later.')
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
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Your recipe has been updated')
            return redirect("recipe")
            messages.error(request, 'There was a problem. Try again later.')
    form = RecipeForm(instance=recipe)
    context = {
        'form': form
    }
    return render(request, 'edit_recipe.html', context)


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe deleted')
    return redirect("recipe")
    messages.error(request, 'Recipe not deleted. Try again later.')
