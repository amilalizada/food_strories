from rest_framework.views import APIView
from ..models import Recipe, Category
from .serializers import RecipeReadSerializer, CategorySerializer, RecipeCreateSerializer

from django.http import JsonResponse

class RecipeApiView(APIView):

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = RecipeCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse(serializer.errors, status=400, safe=False)

    def get(self, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = RecipeReadSerializer(recipes, context={"request": self.request}, many=True)

        return JsonResponse(serializer.data, safe=False)

        # for recipe in recipes:
        #     recipes_dict_data.append({
        #         "title": recipe.title,
        #         "image": recipe.image.url,
        #         "short_description": recipe.short_description,
        #         "long_description": recipe.long_description,
        #         "author": {
        #             "name": recipe.author.username,
        #             "id": recipe.author.id
        #         },
        #         "category": {
        #             "id": recipe.category.id,
        #             "title": recipe.category.title
        #         }
        #     })

        # return JsonResponse(recipes_dict_data, safe=False)


class CategoryApiView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, context={"request": self.request}, many=True)

        return JsonResponse({
            "categories": serializer.data,
            "status": 200
        })


