from django.shortcuts import render
from django.http from django.http import JsonResponse
from .models import CachedCharacters

# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})

def forum(request):
    return render(request, "pages/forum.html", {})

def loginpage(request):
    return render(request, "pages/Marvel_LoginPage.html", {})


# Creates auto guess feature

def character_name_suggestions(request):
    query = request.GET.get('query', '')
    suggestions = CachedCharacters.objects.fil;ter(name__icontains=query)[:3]  #Gets up to 3 suggestions
    suggestion_list = [character.name for charachter in suggestions]
    return JsonResponse({'suggestions': suggestion_list})
    