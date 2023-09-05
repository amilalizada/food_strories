from django import forms
from django import forms
from .models import Recipe

class CreateRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            "title",
            "image",
            "short_description",
            "long_description",
            "category",
            "tag"
        )