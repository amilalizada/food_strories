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
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Recipe
        fields = (
            "title",
            "image",
            "short_description",
            "long_description",
            "author",
            "category",
            "tag",
        )

    def validate(self, attrs):
        if len(attrs) != len(self.context["request"].data):
            raise serializers.ValidationError("You must provide all fields")
        attrs["author_id"] = self.context["request"].user.id

        return attrs
    

class CustomTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    class Meta:
        fields = (
            "refresh",
            "access",
        )