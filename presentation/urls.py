from django.urls import path

from presentation import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('hers_presentation/',views.hers,name='hers'),
    path('hert/',views.hert,name='hert'),
    path('thank/',views.thank,name='thank'),
]
