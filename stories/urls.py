from django.urls import path
from stories.views import (recipes, 
like_recipe, get_recipe, liked_recipes, 
RecipeListView, RecipeDetailView, 
CreateRecipeView, UpdateRecipeView
)

app_name = "stories"
urlpatterns = [
    # path("", recipes, name="recipes"),
    path("", RecipeListView.as_view(), name="recipes"),

    path("like-recipe/<int:id>/", like_recipe, name="like_recipe"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="get_recipe"),
    path("create-recipe/", CreateRecipeView.as_view(), name="create_recipe"),
    path("update-recipe/<int:pk>/", UpdateRecipeView.as_view(), name="update_recipe"),
    path("liked-recipes/", liked_recipes, name="liked_recipes"),
]