from django.db import models


class CommonItem(models.Model):
    category = models.ForeignKey('categories.Category', 
                               on_delete=models.SET_NULL, 
                               null=True, 
                               related_name='common_items')
    image = models.URLField(null=True, blank=True)
    item_name = models.CharField(max_length=255, null=True)
    item_notes = models.TextField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item_name or 'Unnamed Item' 