from rest_framework import viewsets

from .models import Category, CommonItem, GroceryStore, GroceryStoreItem
from .serializers import CategorySerializer, CommonItemSerializer, GroceryStoreItemSerializer, GroceryStoreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommonItemViewSet(viewsets.ModelViewSet):
    queryset = CommonItem.objects.all()
    serializer_class = CommonItemSerializer

class GroceryStoreViewSet(viewsets.ModelViewSet):
    queryset = GroceryStore.objects.all()
    serializer_class = GroceryStoreSerializer

class GroceryStoreItemViewSet(viewsets.ModelViewSet):
    queryset = GroceryStoreItem.objects.all()
    serializer_class = GroceryStoreItemSerializer 