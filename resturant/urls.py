

from django.contrib import admin
from django.urls import path
from django.views import *
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name='resturant'
urlpatterns = [
    
    path('home/',HomePage.as_view(),name='home_page'),
    path('add/menu/',AddMenu.as_view(),name='add_menu'),
    path('update/menu/<int:pk>',EditMenu.as_view(),name='edit_menu'),
    path('delete/menu/<int:pk>',DeleteMenu.as_view(),name='delete_menu'),
    path('list/',MenuList.as_view(),name='menu_list'),
    path('add/ingredient/',AddIngredient.as_view(),name='add_ingredient'),
    path('update/ingredient/<int:pk>',EditIngredient.as_view(),name='edit_ingredient'),
     path('ingredient/list/',IngredientList.as_view(),name='ingredient_list'),
       path('order/list/', OrderList.as_view(), name='order_list'),
    path('add/order/', AddOrder.as_view(), name='add_order'),
       path('add-recipe-requirement/<int:menu_item_id>/',AddRecipe.as_view(),name='add_recipe'),
        path('recipe/list/',RecipeList.as_view(),name='recipe_list'),
        #path('calculation/',calculate_ingredient_used,name="calculate"),
      
        
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
