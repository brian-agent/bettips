from django.urls import path,URLPattern
from . import views
urlpatterns= [

    path('',views.home,name='home'),
    path('all_games',views.all_games,name='all_games'),
    path('yesterday_games',views.yesterday_games,name='yesterday_games'),
    path('previous_two_days_games',views.previous_two_days_games,name='previous_two_days_games'),
    path('previous_three_days_games',views.previous_three_days_games,name='previous_three_days_games'),
    path('previous_four_days_games',views.previous_four_days_games,name='previous_four_days_games'),


]