# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, basilPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('basil/', basilPageView, name='basil'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
