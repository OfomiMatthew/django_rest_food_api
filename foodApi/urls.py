from django.urls import path 
from . import views 

urlpatterns = [
    # path('food-items',views.FoodItemsView.as_view()),
    path('food-items/<int:id>',views.single_item),
    path('food-items/',views.food_item),
]
