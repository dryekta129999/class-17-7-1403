from django.urls import path

from . import views
from .views import *

app_name = 'food'


urlpatterns = [
    path('pizza/',views.show_pizza,name='pizza'),
    path('berenjmorgh/',views.berenjmorgh,name='berenjmorgh'),
    path('hamburger',views.hamburger,name='hamburger'),
]