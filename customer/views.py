from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from issues.models import Issue
from .serializers import UserIssueSerializer
from accounts.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def MyIssues(request):
    return render(request, 'customer/myIssues.html') 

@login_required
def Customers(request):
    return render(request, 'customer/Customers.html') 

@login_required
def booksTable(request):
    return render(request, 'customer/book.html') 

@api_view(['GET'])
def UserIssueAPI(request):
    users = Issue.objects.filter(id=1)
    serializer = UserIssueSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['GET'])
def UserAPI(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)