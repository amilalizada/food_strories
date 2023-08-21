from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Recipe, Story
# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }

    return render(request, "recipes.html", context=context)


def like_recipe(request, id):
    messages.success(request, "Recipe liked")
    existing_ids = request.session.get("liked_recipes", "")
    existing_ids = existing_ids + ' ' + str(id)
    request.session["liked_recipes"] = existing_ids.strip()

    return redirect(reverse_lazy("stories:recipes"))

def liked_recipes(request):
    ids = list(map(int, request.session["liked_recipes"].split()))
    recipes = Recipe.objects.filter(id__in=(ids))
    context={
        "recipes": recipes
    }
    
    return render(request, "liked-recipes.html", context)

def get_recipe(request, id):
    print(id),
    print("-----------")   
    print(type(id)) 

    return render(request, "single.html")