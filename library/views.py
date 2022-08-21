from django.shortcuts import render
from .models import Book, Book,Category,Shelf
from .serializers import BookSerializer,CategorySerializer,ShelfSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def Index(request):
    return render(request, 'base.html')

@login_required
def Books(request):
    return render(request, 'library/books.html')
@login_required   
def Categorys(request):
    return render(request, 'library/category.html')
@login_required
def shelfs(request):
    return render(request, 'library/shelfs.html')   

@api_view(['GET'])
def BookAPI(request):
    Books = Book.objects.all()
    serializer = BookSerializer(Books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def BooksDetailsAPI(request, id):
    BookDetails = get_object_or_404(Book, id=id)
    serializer = BookSerializer(BookDetails, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddBookAPI(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditBookAPI(request, id):
    Book = get_object_or_404(Book, id=id)
    serializer = BookSerializer(Book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteBookAPI(request, id):
    if request.is_ajax():
        Book = get_object_or_404(Book, id=id)
        Book.delete()
        return Response('Book successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Book Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def CategoryAPI(request):
    Categorys = Category.objects.all()
    serializer = CategorySerializer(Categorys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def CategorysDetailsAPI(request, id):
    Category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(Category, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddCategoryAPI(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditCategoryAPI(request, id):
    Category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(Category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteCategoryAPI(request, id):
    if request.is_ajax():
        Category = get_object_or_404(Category, id=id)
        Book.delete()
        return Response('Category successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Category Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def ShelfAPI(request):
    Shelfs = Shelf.objects.all()
    serializer = CategorySerializer(Shelfs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def ShelfsDetailsAPI(request, id):
    ShelfDetails = get_object_or_404(Shelf, id=id)
    serializer = ShelfSerializer(ShelfDetails, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddShelfAPI(request):
    serializer = ShelfSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditShelfAPI(request, id):
    editShelf = get_object_or_404(Shelf, id=id)
    serializer = ShelfSerializer(editShelf, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)



@api_view(['DELETE'])
def DeleteShelfAPI(request, id):
    shelf = get_object_or_404(Shelf, id=id)
    shelf.delete()
    return Response('Shelf successfully Deleted!', status=status.HTTP_200_OK)

