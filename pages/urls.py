from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path("forum/", views.forum, name="forum"),
    path("loginpage/", views.loginpage, name="loginpage")
]