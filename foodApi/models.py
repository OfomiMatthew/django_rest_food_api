from django.db import models

# Create your models here.

 
class Category(models.Model):
  slug = models.SlugField()
  title = models.CharField(max_length=300) 
  
  def __str__(self):
    return self.title
  
class FoodItem(models.Model):
  
  
    
  name= models.CharField(max_length=100)
  description = models.TextField()
  category = models.ForeignKey(Category,on_delete=models.PROTECT)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.SmallIntegerField()
  
  def __str__(self):
    return self.name

 

  
