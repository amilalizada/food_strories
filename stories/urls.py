from django.urls import path
from stories.views import recipes, like_recipe, get_recipe, liked_recipes

app_name = "stories"
urlpatterns = [
    path("", recipes, name="recipes"),
    path("like-recipe/<int:id>/", like_recipe, name="like_recipe"),
    path("recipe/<int:id>/", get_recipe, name="get_recipe"),
    path("liked-recipes/", liked_recipes, name="liked_recipes"),
]