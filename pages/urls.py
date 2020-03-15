from django.urls import path

from .views import HomePageView, AboutPageView, RecipesPageView, newPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('recipes/', RecipesPageView.as_view(), name='recipes'),
    path('newPage/', newPageView.as_view(), name='newpage'),
    path('', HomePageView.as_view(), name='home'),
]
