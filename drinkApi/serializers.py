from rest_framework import serializers 
from .models import DrinkItem 

class DrinkSerializer(serializers.Serializer):
  id=serializers.IntegerField()
  title = serializers.CharField(max_length=200)
  
