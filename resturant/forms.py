
# forms.py
from django import forms
from crispy_forms.helper import FormHelper  # Add this import statement
from crispy_forms.layout import Layout, Submit
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price',]
        context_object_name='forms'
        
        labels = {
            'Name': 'Name*',
            'Price': 'Price*',
           
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

   

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields ="__all__"
   
        
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Ingredient'))


# class OrderItemForm(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['order', 'food_item', 'quantity']  # Make sure to include the 'order' field
        
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['ingredient', 'quantity']


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = RecipeRequirement
        fields = ['ingredient', 'quantity']
class OrderItemForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        fields = ("__all__")



class UserLogin(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'name@flowbite.com'}))
    password = forms.CharField(
        label=("Enter Your Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Your Password'}),
    )
