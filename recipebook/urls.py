from . import views
from django.urls import path


urlpatterns = [
    path('display', views.display_recipe, name="recipe"),
]
