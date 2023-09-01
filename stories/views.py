from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Category, Recipe, Story
# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }

    return render(request, "recipes.html", context=context)


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes.html"
    context_object_name = "recipes"
    paginate_by = 2


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "single.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs) # {recipe: object}
        context["categories"] = Category.objects.all()

        return context


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