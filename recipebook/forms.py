
# Code for edit recipe taken from Code Institute Todo App Walkthrough

from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'instructions',
            'image',
            'cuisine',
            'meal'
        ]