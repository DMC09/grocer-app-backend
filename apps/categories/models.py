from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    select_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name 