from django.urls import path
from django.urls import path

from api.views import DrinkList

urlpatterns = [
    path('cocktails/', DrinkList.as_view(), name='drink_list'),
    
]