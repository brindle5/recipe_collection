from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Cuisine(models.Model):
    """ A model for adding cuisine types (british, american, irish, chinese, indian, etc.) """
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    """ A model for adding meal types (breakfast, lunch, dinner, etc.) """
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """ A model for users to add their own recipes """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=False, blank=False)
    instructions = models.TextField(null=False, blank=False)
    image = CloudinaryField(
        "image", default="placeholder", null=False, blank=False)
    cuisine = models.ForeignKey(
        Cuisine, on_delete=models.SET_NULL, null=True, blank=True)
    meal = models.ForeignKey(
        Meal, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
