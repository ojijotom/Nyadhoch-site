
from django.contrib import admin
from django.urls import path
from nyadhochapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('service/', views.service, name='about'),
    path('portfolio/', views.portfolio, name='about'),
]
