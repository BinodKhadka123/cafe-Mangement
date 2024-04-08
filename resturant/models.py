from datetime import timezone
from typing import Any
from django.db import models


class Menu(models.Model):
    name=models.CharField(max_length=20)
     
    price=models.FloatField()
    def __str__(self):
        return self.name 
   
class Purchase(models.Model):
    quantity=models.IntegerField()  
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
class Ingredient(models.Model):
    
    name = models.CharField(max_length=100)
    available_qty = models.IntegerField()
    measurement_unit = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name} - {self.available_qty}"
class RecipeRequirement(models.Model):
     menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='recipe')
     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
     quantity = models.FloatField()
     def __str__(self):
        return f"{self.menu_item.name} - {self.quantity}"

class OrderItem(models.Model):
    food_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    table_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.food_item.name} - {self.table_name}"


    
        
    