from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FoodItem 
from .serializers import FoodItemSerializer

# Create your views here.
@api_view()
def food_item(request):
  items = FoodItem.objects.all()
  serialized_item = FoodItemSerializer(items,many=True)
  return Response(serialized_item.data)
  
class FoodItemsView(generics.ListCreateAPIView):
  queryset = FoodItem.objects.all()
  serializer_class = FoodItemSerializer

class SingleFoodItem(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
  queryset = FoodItem.objects.all()
  serializer_class = FoodItemSerializer
  
