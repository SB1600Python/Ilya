from django.urls import path
from weather.views import weath_v

urlpatterns = [
    path('', weath_v, name='weather'),
    
]