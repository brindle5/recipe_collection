from django.test import TestCase
from .forms import RecipeForm

# Tests based on the Code Institute ToDo App project view tests


class TestRecipeForm(TestCase):

    def test_recipe_title_is_required(self):
        form = RecipeForm({'title': ''})
        self.assertFalse(form.is_valid())

    def test_description_title_is_required(self):
        form = RecipeForm({'description': ''})
        self.assertFalse(form.is_valid())

    def test_description_is_required(self):
        form = RecipeForm({'description': ''})
        self.assertFalse(form.is_valid())

    def test_ingredients_are_required(self):
        form = RecipeForm({'ingredients': ''})
        self.assertFalse(form.is_valid())

    def test_cuisine_is_required(self):
        form = RecipeForm({'cuisine': ''})
        self.assertFalse(form.is_valid())

    def test_meal_is_required(self):
        form = RecipeForm({'meal': ''})
        self.assertFalse(form.is_valid())

    def test_form_names_are_explicit(self):
        form = RecipeForm()
        self.assertEqual(form.Meta.fields, [
            'title',
            'description',
            'ingredients',
            'instructions',
            'cuisine',
            'meal'
            ])
