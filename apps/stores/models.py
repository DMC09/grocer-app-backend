from django.db import models


class GroceryStore(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class GroceryStoreItem(models.Model):
    store = models.ForeignKey(GroceryStore, 
                            on_delete=models.CASCADE, 
                            related_name='items')
    category = models.ForeignKey('categories.Category', 
                               on_delete=models.SET_NULL, 
                               null=True)
    common_item = models.ForeignKey('items.CommonItem', 
                                  on_delete=models.SET_NULL, 
                                  null=True)
    name = models.CharField(max_length=255, null=True)
    image = models.URLField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name} at {self.store.name}" 