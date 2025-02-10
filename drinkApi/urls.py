from django.urls import path 
from . import views

urlpatterns = [
    path('drinks',views.drink_items,name="drink-items"),
    path('users',views.ListUsers.as_view())
]
