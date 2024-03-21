
from django.db.models import F
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import *
from django.views.generic import ListView
from resturant.forms import *
from resturant.models import *
from django.forms import BaseModelForm, inlineformset_factory
from django.forms import modelformset_factory


class HomePage(View):
    def get(self, request):
        return render(request, 'resturant/home_page.html')
class AddMenu(CreateView):
    model = Menu
    form_class=MenuForm
    template_name = "resturant/add_menu.html"
    success_url=reverse_lazy('resturant:home_page')
class EditMenu(UpdateView):
    model = Menu
    form_class = MenuForm 
    template_name = "resturant/update_menu.html"
    success_url=reverse_lazy('resturant:home_page')
class DeleteMenu(DeleteView):
    model = Menu
    template_name = "resturant/delete_menu.html"

class MenuList(ListView):
    model = Menu
    form_class=MenuForm
    context_object_name = 'list'
    template_name='resturant/list_menu.html'
class IngredientList(ListView):
    model = Ingredient
    context_object_name = 'list'
    template_name='resturant/ingredient_list.html'
class AddIngredient(CreateView):
    model = Ingredient
    form_class=IngredientForm
    success_url=reverse_lazy('resturant:ingredient_list')
    template_name = "resturant/add_ingredient.html"
    

class EditIngredient(UpdateView):
    model = Ingredient
    form_class=IngredientForm
    template_name = "resturant/edit_ingredient.html"
    success_url=reverse_lazy('resturant:ingredient_list')

class OrderList(ListView):
    model = OrderItem
    context_object_name = 'list'
    template_name='resturant/order_list.html'
   
    
# class CreateOrder(CreateView):
#     model = OrderItem
#     form_class = OrderItemForm
#     template_name = "resturant/create_order.html"
#     success_url = reverse_lazy('resturant:order_list')
#     def form_valid(self, form):
#         # Save the order item form
#         order_item = form.save(commit=False)

#         # Save the order form separately
#         order_form = OrderForm(self.request.POST)
#         if order_form.is_valid():
#             order = order_form.save(commit=False)
#             order.save()

#             # Associate the order with the order item
#             order_item.order = order
#             order_item.save()

#         return super().form_valid(form)
   

      
    
class RecipeList(ListView):
    model = RecipeRequirement
    context_object_name = 'list'
    template_name='resturant/recipe_list.html'
class AddRecipe(CreateView):
    model = RecipeRequirement
    form_class=RecipeForm
    template_name = "resturant/add_recipe.html"
    success_url = reverse_lazy('resturant:recipe_list')
    def form_valid(self, form):
        menu_item_id = self.kwargs['menu_item_id']
        menu_item = Menu.objects.get(pk=menu_item_id)
        form.instance.menu_item = menu_item
        return super().form_valid(form)
class AddOrder(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "resturant/create_order.html"
    success_url = reverse_lazy('resturant:order_list')

    def form_valid(self, form):
        # Call the parent class's form_valid method to save the form data
        response = super().form_valid(form)

        # After saving the form data, retrieve the order ID (pk) of the created object
        order_id = self.object.pk
        
        try:
            # Retrieve the OrderItem instance with the given ID
            order_item = OrderItem.objects.get(pk=order_id)

            # Get the associated menu item
            menu_item = order_item.food_item

            # Get the recipe requirements for the menu item
            recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item)

            # Calculate ingredient usage and update available quantity
            for requirement in recipe_requirements:
                ingredient = requirement.ingredient
                quantity_used = requirement.quantity * order_item.quantity
                ingredient.available_qty -= quantity_used
                ingredient.save()
            total_price = order_item.quantity * order_item.food_item.price
            context = {
                'total_price': total_price,
            }
                

        except OrderItem.DoesNotExist:
            # Handle the case where the OrderItem does not exist
            # For example, redirect to an error page or display an error message
            return HttpResponseRedirect('/error/')
        
        # Redirect the user to a success page
        return render(self.request, 'resturant/calculation_ingredient.html',context) 
    
    