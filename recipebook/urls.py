from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeCollection.as_view(), name="recipe"),
    path('add', views.add_recipe, name="add_recipe"),
    # path('edit/<recipe_id>', views.edit_recipe, name='edit_recipe'),
]
