from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializers import CocktailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from cocktails.models import Cocktail

# Create your views here.
class DrinkList(APIView):
    def post(self, request):
        cocktails = Cocktail.objects.all()[:20]
        data = CocktailsSerializer(cocktails, many=True).data
        return Response(data)