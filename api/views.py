from django.shortcuts import render

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

def addBookmark():
    raise NotImplementedError

def removeBookmark():
    raise NotImplementedError

def viewBookmarks():
    raise NotImplementedError

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