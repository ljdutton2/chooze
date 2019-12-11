from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='indexview'),
    path('cocktails/', views.DrinkView.as_view(), name='drinkview'),
    path('search/', views.SearchView.as_view(), name='searchview'),
    path('saved/', views.SaveView.as_view(), name='saveview'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
