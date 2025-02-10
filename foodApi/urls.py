from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('food-items',views.FoodItemsView.as_view()),
    path('food-items/<int:id>',views.single_item),
    path('food-items/',views.food_item),
    path('category/<int:pk>/',views.category_detail),
     path('secret',views.secret),
     
    #  uses POST method call
     path('api-auth-token/',obtain_auth_token), # django in-built authentication view for token,
     path('manager-view',views.manager_view),
    path('throttle-check',views.throttle_check),
    path('throttle-check-auth',views.throttle_check_auth),
    # path('menu-items',views.MenuItem.as_view({'get': 'list'})),
]
