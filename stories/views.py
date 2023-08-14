from django.shortcuts import render
from .models import Recipe, Story
# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }

    return render(request, "recipes.html", context=context)


def get_recipe(request, id):
    print(id),
    print("-----------")   
    print(type(id)) 

    return render(request, "single.html")