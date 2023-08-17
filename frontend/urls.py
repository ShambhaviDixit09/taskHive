from django.contrib import admin
from django.urls import path
from frontend.views import *
from userauth import views


urlpatterns = [
    path('home',home),
    path('',landing),
    path('Signup',views.Signup),
    path('login',views.login_page),
    path('logout/',views.logout_page),
    path('delete/<id>/',delete_task)
    # Your other URL patterns go here...
]