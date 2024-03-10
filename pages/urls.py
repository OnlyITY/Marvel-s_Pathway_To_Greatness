from django.urls import path, include
from pages import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("forum/", views.forum, name="forum"),
    path("loginpage/", views.loginpage, name="loginpage"),
    path('search-suggestions/', views.character_name_suggestions, name = 'search_suggestions'),
    path("test/", views.test, name="test"),
    path("api/", include("api.urls")),
    path('friends/', views.friends_list, name='friends_list'),
    path('add-friend/<int:friend_id>/', views.add_friend, name='add_friend'),
]