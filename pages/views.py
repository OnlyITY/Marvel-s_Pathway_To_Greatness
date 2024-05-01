from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect

from api.MarvelComics.marvelAPI import MarvelAPI
from api.MarvelComics.Marvel import Marvel
from pages.models import Characters, Comics
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from .models import Friendship, Users

# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})

def forum(request):
    return render(request, "pages/forum.html", {})

def test(request):
    return render(request, "pages/test.html", {})
    
# Bookmark method to return pages/bookmarks.html
@login_required
def bookmark(request):
    return render(request, "pages/bookmarks.html", {})

# Creates auto guess feature

def search(request):
    
    if request.method == "POST":
        characterName = str(request.POST.get('characterName', ''))
        year = str(request.POST.get('year', ''))

        if characterName != '' and year != '':
            #marvelApi = MarvelAPI()
            #data = marvelApi.getCharcterInfo(characterName)
            #return render(request, "pages/searchresults.html", {"data": data})
            myMarvel = Marvel()
            data = myMarvel.getCharacter(characterName)
        if characterName != '':
            #marvelApi = MarvelAPI()
            #data = marvelApi.getCharcterInfo(characterName)         
            myMarvel = Marvel()
            name, image, charId, description, c = myMarvel.getCharacter(characterName)
            comInfo =  Comics.objects.filter(characters_id = charId)
            #getName = Characters.objects()
            a = myMarvel.getComics(charId, instance=c)

            PARAMS = {
                'name': name,
                'image': image,
                'id': charId,
                'description': description,
                'comInfo': comInfo,
            }
            return render(request, "pages/searchresults.html", PARAMS)
            #return render(request, "pages/searchresults.html", {"data": data})
        else:
            marvelApi = MarvelAPI()
            data = marvelApi.getCharcters()
            return render(request, "pages/searchresults.html", {"data": data})
    else:
        return render(request, "pages/home.html")



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
    friend = Users.objects.get(id=friend_id)

    if user != friend:
        Friendship.objects.get_or_create(user=user, friend=friend)

    return redirect('friends_list')


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            return HttpResponseRedirect("/accounts/thanks/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, "pages/Register_Feature.html", {"form": form})


def thanks(request):
    return render(request, "pages/Thanks.html")
# Bookmark method with @login_required


def checkout():
    return None
