from django.shortcuts import render
from django.http import JsonResponse
from pages.models import Characters

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
    