from django.test import TestCase
from . import views
from .models import Cuisine, Meal, Recipe


class TestViews(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
