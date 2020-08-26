from django.urls import path
from . import views  # used . because views and urls are in the same folder

urlpatterns = [
    path('main/', views.main, name='main'),
    path('add/', views.add),
    path('show/', views.show)
]
