from django.urls import path
from . import views

urlpatterns = [
    path('recettes', views.recipe_list, name='recipe_list'),
    path('recettes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recettes/new', views.add_recipe, name='add_recipe'),
    path('recettes/search', views.search_recipe, name="search_recipe"),
    path('',views.home,name='home')
]