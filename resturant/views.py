from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import *
from django.views.generic import ListView
from resturant.forms import *
from resturant.models import *
from django.forms import inlineformset_factory
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





