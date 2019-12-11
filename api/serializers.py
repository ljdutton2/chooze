from rest_framework.serializers import ModelSerializer
from cocktails.models import Cocktail

class CocktailsSerializer(ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'
