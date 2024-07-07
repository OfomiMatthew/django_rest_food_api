from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from .models import FoodItem, Category
from .serializers import FoodItemSerializer, CategorySerializer
from rest_framework.renderers import TemplateHTMLRenderer



@api_view(['GET','POST'])
def food_item(request):
  if request.method == 'GET':
    items = FoodItem.objects.select_related('category').all()
    category_name = request.query_params.get('category') #filtering operation
    price_amount = request.query_params.get('price_amount') #filtering operation
    search = request.query_params.get('search')
    ordering = request.query_params.get('ordering')
    if (category_name):
      items = items.filter(category__title=category_name)
      print(items)
    if price_amount:
      items = items.filter(price=price_amount)
    if search:
      items = items.filter(name__contains=search)
    if ordering:
      ordering_fields = ordering.split(',')
      items = items.order_by(*ordering_fields) #use comma to sort using different parameters
      
    
        
      
      
    serialized_item = FoodItemSerializer(items,many=True,context={'request':request})
    return Response(serialized_item.data) 
  if request.method =='POST':
     serialized_item = FoodItemSerializer(data=request.data)
     serialized_item.is_valid(raise_exception=True)
     serialized_item.validated_data
     serialized_item.save()
     return Response(serialized_item.data,status.HTTP_201_CREATED)
    
  
    
  
# class FoodItemsView(generics.ListCreateAPIView):
#   queryset = FoodItem.objects.all()
#   serializer_class = FoodItemSerializer

@api_view()
def single_item(request,id):
  item = get_object_or_404(FoodItem,id=id)
  serialized_item = FoodItemSerializer(item)
  return Response(serialized_item.data)


@api_view()
def category_detail(request,pk):
  category = get_object_or_404(Category,pk=pk)
  serialized_category = CategorySerializer(category)
  return Response(serialized_category.data)


# class SingleFoodItem(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
#   queryset = FoodItem.objects.all()
#   serializer_class = FoodItemSerializer
  
