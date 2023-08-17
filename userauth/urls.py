from django.contrib import admin
from django.urls import path, include
from userauth.views import *
from frontend import views

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('Signup/', Signup, name='Signup'),
    path('home',views.home,name = 'home'),
    path('',views.landing,name = 'landing'),
    path('logout/',logout_page,name = 'logout_page')
]
