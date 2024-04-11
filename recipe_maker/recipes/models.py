from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.ManyToManyField(Ingredient)
    foodDescription = models.CharField(max_length=500)
    recipe = models.CharField(max_length=500)
    
    class Meta:
        ordering = ['name']
        
    
        
    