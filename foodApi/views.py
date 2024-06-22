from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FoodItem 
from .serializers import FoodItemSerializer


@api_view()
def food_item(request):
  items = FoodItem.objects.select_related('category').all()
  serialized_item = FoodItemSerializer(items,many=True)
  return Response(serialized_item.data)
  
# class FoodItemsView(generics.ListCreateAPIView):
#   queryset = FoodItem.objects.all()
#   serializer_class = FoodItemSerializer

@api_view()
def single_item(request,id):
  item = get_object_or_404(FoodItem,id=id)
  serialized_item = FoodItemSerializer(item)
  return Response(serialized_item.data)


# class SingleFoodItem(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
#   queryset = FoodItem.objects.all()
#   serializer_class = FoodItemSerializer
  
