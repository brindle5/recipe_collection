
# Code for edit recipe taken from Code Institute Todo App Walkthrough

from django import forms
from .models import Cuisine, Meal, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'author',
            'description',
            'ingredients',
            'instructions',
            'cuisine',
            'meal'
        ]
