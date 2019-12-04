from django.urls import path

from . import views

urlpatterns = [
    path('', views.DrinkView.as_view(), name='drinkview'),
    # path('search/', views.ingredient, name='ingredient')
]