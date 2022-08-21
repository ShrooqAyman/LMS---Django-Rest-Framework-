from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Issue
from .serializers import IssueSerializer
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
def IssueBook(request):
    return render(request, 'issues/issueBook.html') 


@api_view(['GET'])
def UserAPI(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['GET'])
def IssueAPI(request):
    Issues = Issue.objects.all()
    serializer = IssueSerializer(Issues, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def IssuesDetailsAPI(request, id):
    IssueDetails = get_object_or_404(Issue, id=id)
    serializer = IssueSerializer(IssueDetails, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddIssueAPI(request):
    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditIssueAPI(request, id):
    issue = get_object_or_404(Issue, id=id)
    serializer = IssueSerializer(issue, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteIssueAPI(request, id):
    if request.is_ajax():
        issue = get_object_or_404(Issue, id=id)
        issue.delete()
        return Response('Issue successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Issue Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)
