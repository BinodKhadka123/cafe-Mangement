inventory btorder a-id-recipe-table-ingridient -o

 {{ form.as_p }}
 order_id = self.object.pk
        
        try:
            
            order_item = OrderItem.objects.get(pk=order_id)
            menu_item = order_item.food_item
            recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item)
            for requirement in recipe_requirements:
                ingredient = requirement.ingredient
                quantity_used = requirement.quantity * order_item.quantity
                ingredient.available_qty -= quantity_used
                ingredient.save()
                qty=order_item.quantity
                price=order_item.food_item.price
                food_name=requirement.menu_item.name
            total_price = qty* price
            context = {
                'total_price': total_price,
                'qty':qty,
                'price':price,
                'food_name':food_name
               
               
            }
                

        except OrderItem.DoesNotExist:
            # Handle the case where the OrderItem does not exist
            # For example, redirect to an error page or display an error message
            return HttpResponseRedirect('/error/')
        
        # Redirect the user to a success page
        return render(self.request, 'resturant/calculation_ingredient.html',context) 
    
    