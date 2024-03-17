from datetime import timezone
from django.db import models


class Menu(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
   
class Purchase(models.Model):
    quantity=models.IntegerField()  
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
class Ingredient(models.Model):
    
    name = models.CharField(max_length=100)
    available_qty = models.IntegerField()
class RecipeRequirement(models.Model):
    ingrident_measurement_id=models.ForeignKey(Ingredient,on_delete=models.CASCADE) 
    menu_item_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
class IngridentMeasurement(models.Model):
    name=models.CharField(max_length=20)
    quantity=models.IntegerField()  
    ingrident=models.ForeignKey(Ingredient,on_delete=models.CASCADE) 
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
class MeasurementUnit(models.Model):

    unit_choices=[ ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('lb', 'Pound'),
        ('oz', 'Ounce'),

    ]
    name=models.CharField(max_length=20,choices=unit_choices)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()