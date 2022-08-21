from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('books', views.Books, name="Books"),
    path('shelfs', views.shelfs, name="shelfs"),
    path('categorys', views.Categorys, name="categorys"),

    path('api/Books/', views.BookAPI, name="BookAPI"),
    path('api/Books/add/', views.AddBookAPI, name="AddBookAPI"),
    path('api/Books/<int:id>/', views.BooksDetailsAPI, name="BooksDetailsAPI"),
    path('api/Books/edit/<int:id>/', views.EditBookAPI, name="EditBookAPI"),
    path('api/Books/delete/<int:id>/', views.DeleteBookAPI, name="DeleteBookAPI"),

    path('api/Categorys/', views.CategoryAPI, name="CategoryAPI"),
    path('api/Category/add/', views.AddCategoryAPI, name="AddCategoryAPI"),
    path('api/Category/<int:id>/', views.CategorysDetailsAPI, name="CategorysDetailsAPI"),
    path('api/Category/edit/<int:id>/', views.EditCategoryAPI, name="EditCategoryAPI"),
    path('api/Category/delete/<int:id>/', views.DeleteCategoryAPI, name="DeleteCategoryAPI"),

    path('api/shelfs/', views.ShelfAPI, name="ShelfAPI"),
    path('api/shelf/add/', views.AddShelfAPI, name="AddShelfAPI"),
    path('api/shelf/<int:id>/', views.ShelfsDetailsAPI, name="ShelfsDetailsAPI"),
    path('api/shelf/edit/<int:id>/', views.EditShelfAPI, name="EditShelfAPI"),
    path('api/shelf/delete/<int:id>/', views.DeleteShelfAPI, name="DeleteShelfAPI"),

  
]