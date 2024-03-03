from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from pages.models import Bookmarks, Users
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from datetime import datetime
# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})

def registerUser():
    raise NotImplementedError

def logIn():
    raise NotImplementedError

def logOut():
    raise NotImplementedError

def createNewPost():
    raise NotImplementedError

def viewPosts():
    raise NotImplementedError

def searchByArc():
    raise NotImplementedError

def searchByName():
    raise NotImplementedError

def searchByDecade():
    raise NotImplementedError

@csrf_exempt
def addBookmark(request, user_id):
    if request.method == "POST":
        link = request.POST.get('link', False)
        b = Bookmarks(link=link, user_id=user_id, creationDate=datetime.now())
        b.save()
        return HttpResponse("Bookmark has been added.")

def removeBookmark(request, bookmark_id, user_id):
    bookmark = Bookmarks.objects.get(id=bookmark_id)
    if bookmark:
        bookmark.delete()
        return HttpResponse("Bookmark has been removed.")
    else:
        return HttpResponseNotFound("Bookmark does not exist.")


async def viewBookmarks(request, user_id):
    u = await Users.objects.filter(id=user_id).afirst()
    if u:
        bookmarks = [b.link async for b in Bookmarks.objects.filter(user_id=user_id)]
        response_data = {"bookmarks": bookmarks}
        return JsonResponse(response_data, status=200)
    else:
        return HttpResponseNotFound("User does not exist.")

def addReview():
    raise NotImplementedError

def viewReviews():
    raise NotImplementedError

def averageRating():
    raise NotImplementedError

def addAppearance():
    raise NotImplementedError

def characterDetails():
    raise NotImplementedError

def characterTimeline():
    raise NotImplementedError

def addForSale():
    raise NotImplementedError

def removeFromSale():
    raise NotImplementedError

def viewInventoryOfSale():
    raise NotImplementedError