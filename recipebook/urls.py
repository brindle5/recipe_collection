from . import views
from django.urls import path
from recipebook import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('display', views.display_recipe, name="recipe"),
]
