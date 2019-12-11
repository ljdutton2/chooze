from django.shortcuts import render
from django.http import HttpResponse
import requests
from cocktails.models import Cocktail
import os
from dotenv import load_dotenv
from django.views import View
load_dotenv()

COCKTAIL_API_KEY = os.getenv('COCKTAIL_API_KEY')

class IndexView(View):
    def get(self, request):
        return render(request, 'cocktails/index.html')

class DrinkView(View):
    def get(self, request):
        random_cocktail = requests.get(f'https://www.thecocktaildb.com/api/json/v2/{COCKTAIL_API_KEY}/random.php')

        if random_cocktail.status_code == 200:
            response = random_cocktail.json()['drinks'][0]
            name = response['strDrink']
            instructions = response['strInstructions']
            image = response['strDrinkThumb']
            ing1= response['strIngredient1']
            ing2= response['strIngredient2']
            ing3= response['strIngredient3']
            ing4= response['strIngredient4']

        

        return render(request, 'cocktails/home2.html', {
            'name':name,
            'instructions': instructions,
            'image': image,
            'ing1': ing1,
            'ing2': ing2,
            'ing3': ing3,
            'ing4': ing4

        })

class SearchView(View):
    def post(self, request):
        drink_name = request.POST['name']
        cocktail = requests.get(f'https://www.thecocktaildb.com/api/json/v2/{COCKTAIL_API_KEY}/filter.php?i={drink_name}')
        if cocktail.status_code == 200:
            response = cocktail.json()['drinks']
        
        if response == 'None Found':
            return render(request, 'cocktails/search.html')
        
        return render(request, 'cocktails/search.html', {
            'drinks': response,
        })


    def get(self, request):
        return render(request, 'cocktails/search.html')

class SaveView(View):
    def post(self,request):
        return render(request,'cocktails/saved.html')