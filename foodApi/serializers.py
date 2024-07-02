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
    
  
  

class FoodItemSerializer(serializers.HyperlinkedModelSerializer):
  stock = serializers.IntegerField(source="inventory")
  price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  # category = serializers.HyperlinkedRelatedField(
  #   queryset=Category.objects.all(),
  #   view_name='category-detail'
   
  # )
  # category = serializers.StringRelatedField() #use this for a single field in the category class model based on the string method
  category = CategorySerializer(read_only=True) #read_only =True means I do not need to add this field when creating a POST
  category_id = serializers.IntegerField(write_only=True) #adding new category in addition to ones already created
  class Meta:
    model = FoodItem
    fields = ['id','name','description','price','stock','category','price_after_tax','category_id']
    # depth=1
    
  def calculate_tax(self,product:FoodItem):
    return product.price * Decimal(1.1)