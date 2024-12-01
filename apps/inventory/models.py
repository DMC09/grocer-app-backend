from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class CommonItem(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Category', 
                                  on_delete=models.SET_NULL, 
                                  null=True,
                                  related_name='common_items')
    image = models.URLField(null=True, blank=True)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    item_notes = models.TextField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item_name or 'Unnamed Item'

class GroceryStore(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class GroceryStoreItem(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    category_id = models.ForeignKey('Category', 
                                  on_delete=models.SET_NULL, 
                                  null=True)
    common_item_id = models.ForeignKey('CommonItem', 
                                     on_delete=models.SET_NULL, 
                                     null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.URLField(null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)
    store_id = models.ForeignKey('GroceryStore', 
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='items')

    def __str__(self):
        return f"{self.name} at {self.store_id.name if self.store_id else 'Unknown Store'}" 