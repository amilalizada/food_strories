from django.contrib import admin
from .models import Category, Tag, Recipe, Story
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register([Tag, Story])

class RecipeCategoryInline(admin.TabularInline):
    model = Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [RecipeCategoryInline]


class RecipeAdmin(TranslationAdmin):
    search_fields = ["title", "short_description"]
    list_display = ["title", "get_photo", "slug", "short_description", "author"]
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
    

admin.site.register(Recipe, RecipeAdmin)

