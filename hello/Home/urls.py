from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('',views.index,name='Home'),
    path('about',views.about,name='about'),
    path('icecreams',views.icecreams,name='icecreams'),
    path('softies',views.softies,name='softies'),
    path('IcecreamCakes',views.IcecreamCakes,name='IcecreamCakes'),
    path('contact',views.contact,name='contact')
]
