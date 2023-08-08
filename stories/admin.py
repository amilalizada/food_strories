from django.contrib import admin
from .models import Category, Tag, Recipe, Story
from django.utils.html import format_html
# Register your models here.

admin.site.register([Tag, Story])

class RecipeCategoryInline(admin.TabularInline):
    model = Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [RecipeCategoryInline]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ["title", "short_description"]
    list_display = ["title", "get_photo", "short_description", "author"]
    list_filter = ["category", "tag", "author"]
    fieldsets = (
        (
            "Information",
            {
                "fields": ("title", "image", "short_description", "long_description",)
            },
        ),
        (
            "Relations",
            {
                "fields": ("category", "author", "tag")
            },
        ),
    )

    def get_photo(self, obj):
        img_str = f"<img src='{obj.image.url}' width='100px'>"
        return format_html(img_str)
