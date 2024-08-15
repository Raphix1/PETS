from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('cats/', views.view_cats),
    path('dogs/', views.view_dogs),
    path('hamsters/', views.view_hamsters),


]