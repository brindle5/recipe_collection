from django.contrib import admin
from .models import Cuisine, Meal, Recipe


admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Recipe)
