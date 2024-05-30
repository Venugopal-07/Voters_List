from django.urls import path
from . import views

urlpatterns = [
    path('', views.voter_list, name='voter_list'),
]