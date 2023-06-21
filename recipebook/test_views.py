from django.test import TestCase
from . import views
from .models import Cuisine, Meal, Recipe

class TestViews(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_add_recipe_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')
    
    # def test_get_edit_recipe_page(self):
    #     recipe = Recipe.objects.create(name="Test Recipe")
    #     response = self.client.get(f'/edit/{recipe.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'edit_recipe.html')

    # def test_can_add_recipe(self):
    #     response = self.client.post('/add', {'name': 'Test Add Recipe'})
    #     self.assertRedirects(response='/')

    # def test_can_edit_recipe(self):
    #     response = self.client.post('/edit', {'name': 'Test Edit Recipe'})
    #     self.assertRedirects(response='/')

    # def test_can_delete_recipe(self):
    #     recipe = Recipe.objects.create(name="Test Recipe")
    #     response = self.client.get(f'/delete/{recipe.id}')
    #     self.assertRedirects(response='/')
    #     existing_items = Recipe.objects.filter(id=item.id)
    #     self.assertEqual(len(existing_items), 0)
    
