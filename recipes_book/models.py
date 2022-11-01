from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_body = models.TextField()
    dish_image = models.ImageField(upload_to="dish_photos/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return f"{self.recipe_name}"
