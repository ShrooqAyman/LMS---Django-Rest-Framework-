from django.urls import path
from . import views

urlpatterns = [
    path('api/UserIssueAPI/', views.UserIssueAPI, name="UserIssueAPI"),
    path('api/UserAPI/', views.UserAPI, name="UserAPI"),
    path('myIssues/', views.MyIssues, name="MyIssues"),
    path('booksTable/', views.booksTable, name="booksTable"),
    path('customers/', views.Customers, name="Customers"),
    

  
]