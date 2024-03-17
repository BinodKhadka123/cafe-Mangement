# forms.py
from django import forms
from crispy_forms.helper import FormHelper  # Add this import statement
from crispy_forms.layout import Layout, Submit
from .models import *

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price']
        
        labels = {
            'name': 'Name*',
            'price': 'Price*',
        }

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Menu'))

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
       
        
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Ingredient'))
class PurchaseForm(forms.ModelForm):
    
    class Meta:
        model = Purchase
        fields = ("__all__")

