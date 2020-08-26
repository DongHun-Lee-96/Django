from django.urls import path
from . import views  # used . because views and urls are in the same folder

urlpatterns = [
    path('hospital/', views.hospital)
]
