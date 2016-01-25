from django.db import models
from django.contrib.auth.models import User



class ShoppingList(models.Model):
    user = models.ForeignKey(User, related_name="shopping_list")
    title = models.TextField(max_length=30)
    created = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
