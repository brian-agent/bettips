from django.urls import path,URLPattern
from . import views
urlpatterns= [

    path('',views.home,name='home'),
    path('all_games',views.all_games,name='all_games')


]