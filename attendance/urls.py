from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.cache import never_cache


app_name = 'attendance'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', never_cache(views.login_user), name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home', views.home, name='home'),
    path('add/<int:subject>/<int:where>', views.add, name='add'),
]