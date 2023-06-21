from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeCollection.as_view(), name="recipe"),
    path('add', views.add_recipe, name="add"),
    path('edit/<recipe_id>', views.edit_recipe, name="edit"),
    path('delete/<recipe_id>', views.delete_recipe, name="delete"),
    path('', views.return_home, name="recipe")
]
