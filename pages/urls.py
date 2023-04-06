# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView,  results, homePost, lookUpView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('results/<str:choice>/<str:f_rank1>/<int:gk_score1>/<int:def_score1>/<int:off_score1>/<int:mid_score1>/<str:choice2>/<str:f_rank2>/<int:gk_score2>/<int:def_score2>/<int:off_score2>/<int:mid_score2>/', results, name='results'),
    path('lookUpTable/', lookUpView, name='lookUpTable'),
]