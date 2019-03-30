from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.post,name='posts'),
    path('sports/',views.sports,name='sports'),
]