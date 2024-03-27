from django.urls import path 
from . import views 

urlpatterns = [
    # path('food-items',views.FoodItemsView.as_view()),
    path('food-item/<int:pk>',views.SingleFoodItem.as_view()),
    path('food-items',views.food_item),
]
