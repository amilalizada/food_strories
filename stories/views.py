from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Category, Recipe, Story
from .forms import CreateRecipeForm
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

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get("cat")
        if category_id:
            queryset = queryset.filter(category__id=category_id)
            
        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "single.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context


class CreateRecipeView(LoginRequiredMixin, CreateView):
    template_name = "create_recipe.html"
    form_class = CreateRecipeForm
    success_url = reverse_lazy("stories:recipes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()

        return super().form_valid(form)


class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    template_name = "update_recipe.html"
    model = Recipe
    form_class = CreateRecipeForm
    success_url = reverse_lazy("stories:recipes")

    # def get_queryset(self):

    #     return super().get_queryset()



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