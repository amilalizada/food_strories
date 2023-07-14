from django.contrib import admin
from .models import Category, Tag, Recipe, Story
# Register your models here.

admin.site.register([Category, Tag, Recipe, Story])
