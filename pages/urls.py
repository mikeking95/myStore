from django.urls import path

from .views import HomePageView, AboutPageView, RecipesPageView, newPageView, AnimatedGrid

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('recipes/', RecipesPageView.as_view(), name='recipes'),
    path('newPage/', newPageView.as_view(), name='newpage'),
    path('new/', AnimatedGrid.as_view(), name='new'),
    path('', HomePageView.as_view(), name='home'),
]

