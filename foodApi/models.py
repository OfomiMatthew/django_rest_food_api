from django.db import models

# Create your models here.
class FoodItem(models.Model):
  CATEGORY =[
      ('appetizer', 'Appetizer'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
  ]
    
    
    
  name= models.CharField(max_length=100)
  description = models.TextField()
  category = models.CharField(max_length=20, choices=CATEGORY,default="")
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.SmallIntegerField()
  
  
  
