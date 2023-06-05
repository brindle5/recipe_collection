from . import views
from django.urls import path


urlpatterns = [
    path('display', views.RecipeCollection.as_view(), name="recipe"),
]
