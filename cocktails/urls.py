from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.DrinkView.as_view(), name='drinkview'),
    path('search/', views.SearchView.as_view(), name='searchview'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
