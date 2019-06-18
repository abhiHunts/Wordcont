
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('egg/', views.egg),
    path('counts/', views.count, name='count'),
    path('about/', views.about, name='about')

]
