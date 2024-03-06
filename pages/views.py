from django.shortcuts import render, redirect
from django.http import JsonResponse
from pages.models import Characters
from django.contrib.auth.decorators import login_required
from .models import Friendship

# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})

def forum(request):
    return render(request, "pages/forum.html", {})

def loginpage(request):
    return render(request, "pages/Marvel_LoginPage.html", {})

def test(request):
    return render(request, "pages/test.html", {})


# Creates auto guess feature

def character_name_suggestions(request):
    query = request.GET.get('query', '')
    suggestions = Characters.objects.filter(name__icontains=query)[:3]  #Gets up to 3 suggestions
    suggestion_list = [character.name for character in suggestions]
    return JsonResponse({'suggestions': suggestion_list})

def friends_list(request):
    user = request.user
    friends = user.user_friends.all()
    return render(request, 'forum.html', {'friends': friends})

@login_required
def add_friend(request, friend_id):
    user = request.user
    friend = User.objects.get(id=friend_id)

    if user != friend:
        Friendship.objects.get_or_create(user=user, friend=friend)

    return redirect('friends_list')
    