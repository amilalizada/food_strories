from django.urls import path
from .views import RecipeApiView, CategoryApiView, RecipeListApiView, RecipeDetailApiView


app_name = "stories"
urlpatterns = [
    path("recipes/", RecipeListApiView.as_view(), name="recipes_api"),
    path("recipes/<int:pk>", RecipeDetailApiView.as_view(), name="recipe_detail_api"),
    path("categories/", CategoryApiView.as_view(), name="categories_api"),
]