from rest_framework.response import Response
from .models import DrinkItem
from rest_framework.decorators import api_view
from .serializers import DrinkSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.
@api_view()
def drink_items(request):
  items = DrinkItem.objects.all()
  serialized_item = DrinkSerializer(items,many=True)
  return Response(serialized_item.data)

class ListUsers(APIView):
  def get(self, request):
    usernames = [user.username for user in User.objects.all()]
    return Response(usernames)
