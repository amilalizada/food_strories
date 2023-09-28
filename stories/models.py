from django.db import models
from django.urls import reverse_lazy
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth import get_user_model
# Create your models here.
USER = get_user_model()
class Tag(models.Model):    
    title = CharField(max_length=30)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = CharField(max_length=30)
    image = ImageField(upload_to='media/categories/')

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class Recipe(models.Model):
    title = CharField(max_length=50)
    image = ImageField(upload_to='media/recipies/')
    slug = models.SlugField(max_length=100, null=True)
    short_description = CharField(max_length=200)
    long_description = TextField()
    tag = ManyToManyField(Tag)
    author = ForeignKey(USER, on_delete=models.CASCADE)
    category = ForeignKey(Category,related_name="recipes", on_delete=models.CASCADE)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    
    def get_absolute_url(self):
        return reverse_lazy("stories:get_recipe", kwargs={"pk": self.pk})


class Story(models.Model):
    title = CharField(max_length=50)
    image = ImageField(upload_to='media/stories/')
    long_description = TextField()
    tag = ManyToManyField(Tag)
    author = ForeignKey(USER, on_delete=models.CASCADE)
    category = ForeignKey(Category, related_name="stories", on_delete=models.CASCADE)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title