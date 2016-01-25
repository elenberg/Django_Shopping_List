from django.db import models
from . import ShoppingList

class Item(models.Model):
    TYPE_OPTIONS = (
    (FOOD, 'Food'),
    (CLOTHES, 'Clothes'),
    (ELECTRONICS, 'Electronics'),
    (RECREATION, 'Recreation'),
    (SUPPLIES, 'SUPPLIES'),
    (NONE, "")
    )
    title = models.TextField(max_length=20)
    notes = models.TextField(max_length=100, null=True)
    found = models.BooleanField(default=False)
    type = models.CharField(max_length=30,options=TYPE_OPTIONS, null=True, blank=True)
    on_list = models.ForeignKey(ShoppingList, related_name="items")
