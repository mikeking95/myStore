from django.urls import path

from .views import HomePageView, AboutPageView, RecipesPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('recipes/', RecipesPageView.as_view(), name='recipes'),
    path('', HomePageView.as_view(), name='home'),
]
