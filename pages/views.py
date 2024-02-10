from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})

def forum(request):
    return sender(request, "pages/forum.html", {})

def loginpage(request):
    return sender(request, "pages/Marvel_LoginPage.html", {})