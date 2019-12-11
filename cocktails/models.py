from django.db import models
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
import requests
import os 
from dotenv import load_dotenv
import django.utils.timezone
load_dotenv()


# Create your models here.

COCKTAIL_API_KEY = os.getenv('COCKTAIL_API_KEY')
class Cocktail(models.Model):
    

        
        
        strDrink = models.CharField(max_length=100, primary_key=False)
        idDrink = models.CharField(max_length=100, primary_key=True) 
            # strInstructions = models.TextField()
            # strDrinkThumb = models.URLField()
            # strIngredient1 = models.CharField(max_length=100)
        # strIngredient2 = models.CharField(max_length=100)
        # strIngredient3 = models.CharField(max_length=100)
        # strIngredient4 = models.CharField(max_length=100)
    

def __str__(self):
    return self.strDrink

