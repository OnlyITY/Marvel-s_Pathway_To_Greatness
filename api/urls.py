from django.urls import path
from api import views

urlpatterns = [
    path('User/registerUser/', views.registerUser(), name="registerUser"),
    path('User/logIn/', views.logIn(), name="logIn"),
    path('User/logOut/', views.logOut(), name="logOut"),
    path('Forum/createNewPost/', views.createNewPost(), name="createNewPost"),
    path('Forum/viewPosts/', views.viewPosts(), name="viewPosts"),
    path('Search/searchByArc/', views.searchByArc(), name="searchByArc"),
    path('Search/searchByName/', views.searchByName(), name="searchByName"),
    path('Search/searchByDecade/', views.searchByDecade(), name="searchByDecade"),
    path('Bookmark/addBookmark/', views.addBookmark(), name="addBookmark"),
    path('Bookmark/removeBookmark/', views.removeBookmark(), name="removeBookmark"),
    path('Bookmark/viewBookmarks/', views.viewBookmarks(), name="viewBookmarks"),
    path('ReviewSystem/addReview/', views.addReview(), name="addReview"),
    path('ReviewSystem/viewReviews/', views.viewReviews(), name="viewReviews"),
    path('ReviewSystem/averageRating/', views.averageRating(), name="averageRating"),
    path('ComicCharacter/addAppearance/', views.addAppearance(), name="addAppearance"),
    path('ComicCharacter/characterDetails/', views.characterDetails(), name="characterDetails"),
    path('ComicCharacter/characterTimeline/', views.characterTimeline(), name="characterTimeline"),
    path('SellersInventory/addForSale/', views.addForSale(), name="addForSale"),
    path('SellersInventory/removeFromSale/', views.removeFromSale(), name="removeFromSale"),
    path('SellersInventory/viewInventoryOfSale/', views.viewInventoryOfSale(), name="viewInventoryOfSale")
]
