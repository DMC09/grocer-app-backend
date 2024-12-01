from rest_framework import serializers

from .models import Category, CommonItem, GroceryStore, GroceryStoreItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'quantity', 'select_id']

class CommonItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonItem
        fields = ['id', 'item_name', 'image', 'item_notes', 'select_id', 'category_id']

class GroceryStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryStore
        fields = ['id', 'name', 'image', 'quantity', 'select_id', 'created_at']

class GroceryStoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryStoreItem
        fields = ['id', 'name', 'image', 'notes', 'quantity', 'select_id', 'store_id', 'category_id', 'common_item_id', 'created_at', 'modified_at'] 