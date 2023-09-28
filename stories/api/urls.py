from django.urls import path
from .views import RecipeApiView, CategoryApiView


app_name = "stories"
urlpatterns = [
    path("recipes/", RecipeApiView.as_view(), name="recipes_api"),
    path("categories/", CategoryApiView.as_view(), name="categories_api"),
]