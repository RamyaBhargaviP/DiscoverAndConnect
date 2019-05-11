from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.profilehome,name='profilehome'),
    path('about/',views.about,name='about'),
    
]