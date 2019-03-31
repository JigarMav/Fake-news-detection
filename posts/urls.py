from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.post,name='posts'),
    path('sports/',views.sports,name='sports'),
    path('tech/',views.tech,name='tech'),
    path('health/',views.health,name='health'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.entertain, name='entertain'),
    path('top/',views.top_articles,name='top'),

]