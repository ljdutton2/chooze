from django.db import models


# Create your models here.


class Cocktail(models.Model):

    idDrink = models.AutoField(primary_key=True)
    strDrink = models.CharField(max_length=100)
    strAlcoholic = models.CharField(max_length=100)
    strInstructions = models.TextField()
    strDrinkThumb = models.URLField()
    strIngredient1 = models.CharField(max_length=100)
    strIngredient2 = models.CharField(max_length=100)
    strIngredient3 = models.CharField(max_length=100)
    strIngredient4 = models.CharField(max_length=100)
   

    def __str__(self):
        return self.strDrink

