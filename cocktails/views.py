from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from dotenv import load_dotenv
from django.views import View
load_dotenv()

COCKTAIL_API_KEY = os.getenv('COCKTAIL_API_KEY')



class DrinkView(View):
    def get(self, request):
        random_cocktail = requests.get(f'https://www.thecocktaildb.com/api/json/v2/{COCKTAIL_API_KEY}/random.php')
        
        if random_cocktail.status_code == 200:
            response = random_cocktail.json()['drinks'][0]
        
        name = response['strDrink']
        instructions = response['strInstructions']

        return render(request, 'cocktails/index.html', {
            'name':name,
            'instructions': instructions,
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

# def index(request):
#     random_cocktail = requests.get(f'https://www.thecocktaildb.com/api/json/v2/{COCKTAIL_API_KEY}/random.php')
    
#     if random_cocktail.status_code == 200:
#         response = random_cocktail.json()['drinks'][0]
    
#     name = response['strDrink']
#     instructions = response['strInstructions']

#     return render(request, 'cocktails/home.html', {
#         'name':name,
#         'instructions': instructions
#     })

# def ingredient(request):
#     drink_name = request.POST['name']
#     cocktail = requests.get(f'https://www.thecocktaildb.com/api/json/v2/{COCKTAIL_API_KEY}/filter.php?i={drink_name}')

#     if cocktail.status_code == 200:
#         response = cocktail.json()['drinks']
    
#     return render(request, 'cocktails/home.html', {
#         'drinks': response,
#     })