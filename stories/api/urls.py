from django.urls import path


app_name = "stories"
urlpatterns = [
    # path("", recipes, name="recipes"),
    path("", RecipeListView.as_view(), name="recipes_api"),
]