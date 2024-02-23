from django.urls import path
from pages import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("forum/", views.forum, name="forum"),
    path("loginpage/", views.loginpage, name="loginpage"),
    path('search-suggestions/', views.search_suggestions, name = 'search_suggestions'),
]