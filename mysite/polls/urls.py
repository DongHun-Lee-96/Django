from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # index is used for redirect later
    path('<int:question_id>/', views.detail, name='detail'),
    path('vote/<int:question_id>/', views.vote, name='vote')
]
