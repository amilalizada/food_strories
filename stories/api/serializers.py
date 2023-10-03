from rest_framework import serializers
from ..models import Recipe, Category


class CategorySerializer(serializers.ModelSerializer):
    recipes = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "recipes",
        )

    def get_recipes(self, obj):
        serializer = RecipeCategorySerializer(obj.recipes.all(), context=self.context, many=True)

        return serializer.data
    

class CategoryCreateSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "title",
            "image",
        )
    

class CategoryRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
        )
    

class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "image",
            "short_description",
            "long_description",
            "author",
        )


class RecipeReadSerializer(serializers.ModelSerializer):
    category = CategoryRecipeSerializer()
    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "image",
            "short_description",
            "long_description",
            "author",
            "category",
            "tag",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
        )


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "image",
            "short_description",
            "long_description",
            "author",
            "category",
            "tag",
        )