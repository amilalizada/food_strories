from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Recipe, Category
from .serializers import (
    RecipeReadSerializer, 
    CategorySerializer, 
    RecipeCreateSerializer, 
    CategoryCreateSerilizer,
    CustomTokenSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema


from django.http import JsonResponse


class GenericViewSerializerClassesMixin:
    
    def get_serializer_class(self):
        return self.serializers_classes[self.request.method]


class RecipeListApiView(GenericViewSerializerClassesMixin, ListCreateAPIView):
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticated]
    serializers_classes = {
        "GET": RecipeReadSerializer,
        "POST": RecipeCreateSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__title", "title"]

    # def post(self, request, *args, **kwargs):
    #     print(request.data["image"])
    #     print(request.data)

    #     # request.data["image"] = request.data["image"].split("/")[-1]
    #     return super().post(request, *args, **kwargs)


class RecipeDetailApiView(GenericViewSerializerClassesMixin, RetrieveUpdateDestroyAPIView):
    '''
    RetrieveUpdateDestroyAPIView - GET, PUT, PATCH, DELETE
    '''
    queryset = Recipe.objects.all()
    serializers_classes = {
        "GET": RecipeReadSerializer,
        "PUT": RecipeCreateSerializer,
        "PATCH": RecipeCreateSerializer,
    }


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


class CategoryApiView(GenericViewSerializerClassesMixin, ListCreateAPIView):
    queryset = Category.objects.all()
    serializers_classes = {
        "GET": CategorySerializer,
        "POST": CategoryCreateSerilizer,
    }


class CustomTokenObtainView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: CustomTokenSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



