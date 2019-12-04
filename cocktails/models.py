from django.db import models

# Create your models here.
class Cocktails(models.Model):
    ingredient_num = models.CharField(max_length=200)
    liquor_type = models.CharField(max_length=200)

