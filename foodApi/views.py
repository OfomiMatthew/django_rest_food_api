from django.shortcuts import render
from rest_framework import generics
from .models import FoodItem 
from .serializers import FoodItemSerializer

# Create your views here.

class FoodItemsView(generics.ListCreateAPIView):
  queryset = FoodItem.objects.all()
  serializer_class = FoodItemSerializer

class SingleFoodItem(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
  queryset = FoodItem.objects.all()
  serializer_class = FoodItemSerializer