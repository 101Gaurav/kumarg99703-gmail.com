from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('search',views.searching),
    path("stats",views.stats)
]