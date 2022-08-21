from django.urls import path
from . import views

urlpatterns = [
    path('', views.IssueBook, name="IssueBook"),
    path('api/users/', views.UserAPI, name="UserAPI"),
    path('api/issue/', views.IssueAPI, name="IssueAPI"),
    path('api/issue/add/', views.AddIssueAPI, name="AddIssueAPI"),
    path('api/issue/<int:id>/', views.IssuesDetailsAPI, name="IssuesDetailsAPI"),
    path('api/issue/edit/<int:id>/', views.EditIssueAPI, name="EditIssueAPI"),
    path('api/issue/delete/<int:id>/', views.DeleteIssueAPI, name="DeleteIssueAPI"),
    

  
]