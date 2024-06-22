from rest_framework import serializers
from .models import FoodItem, Category
from decimal import Decimal

# class FoodItemSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = FoodItem
#     fields = ["id","name","description","category","price","inventory"]


# class FoodItemSerializer(serializers.Serializer):
#   id = serializers.IntegerField()
#   name= serializers.CharField(max_length=200)
#   category = serializers.CharField(max_length=20)


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id','slug','title']
    
  
  

class FoodItemSerializer(serializers.ModelSerializer):
  stock = serializers.IntegerField(source="inventory")
  price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  category = CategorySerializer()
  # category = serializers.StringRelatedField() #use thie for a single field in the category class model based on the string method
  class Meta:
    model = FoodItem
    fields = ['id','name','description','price','stock','category','price_after_tax']
    
  def calculate_tax(self,product:FoodItem):
    return product.price * Decimal(1.1)