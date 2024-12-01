from django.contrib import admin
from django.utils.html import format_html

from .models import Category, CommonItem, GroceryStore, GroceryStoreItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'display_image')
    search_fields = ('name',)
    list_filter = ('quantity',)
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image)
        return "No image"
    display_image.short_description = 'Image'

@admin.register(CommonItem)
class CommonItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'category_id', 'display_image')
    list_filter = ('category_id',)
    search_fields = ('item_name', 'item_notes')
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image)
        return "No image"
    display_image.short_description = 'Image'

@admin.register(GroceryStore)
class GroceryStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'created_at', 'display_image')
    search_fields = ('name',)
    list_filter = ('created_at',)
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image)
        return "No image"
    display_image.short_description = 'Image'

class GroceryStoreItemInline(admin.TabularInline):
    model = GroceryStoreItem
    extra = 1
    fields = ('name', 'category_id', 'quantity', 'notes')

@admin.register(GroceryStoreItem)
class GroceryStoreItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'store_id', 'category_id', 'quantity', 'modified_at')
    list_filter = ('store_id', 'category_id', 'created_at', 'modified_at')
    search_fields = ('name', 'notes', 'category')
    readonly_fields = ('created_at', 'modified_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'store_id', 'category', 'category_id', 'common_item_id')
        }),
        ('Details', {
            'fields': ('quantity', 'notes', 'image', 'select_id')
        }),
        ('System Fields', {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image)
        return "No image"
    display_image.short_description = 'Image'
