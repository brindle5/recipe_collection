from django.test import TestCase
from .models import Cuisine, Meal, Recipe

class TestModels(TestCase):

    def test_cuisine_exists(self):
        self.assertContains(Cuisine)
        
        
