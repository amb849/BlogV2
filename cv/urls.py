from django.urls import path
from . import views

urlpatterns = [
    path('', views.CV_list, name='CV_list'),
]