from ast import arg
from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Shelf(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Shelfs'
    
    def __str__(self):
        return self.name
   
class Book(models.Model):
    STATUS =(
        ('available','available'),
        ('non-available','non-available'),
    )

    slug = models.SlugField(max_length=255)
    category= models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    title= models.CharField(max_length=50,null=True)
    isbn = models.CharField(max_length=50,null=True)
    author= models.CharField(max_length=50,null=True)
    shelf= models.ForeignKey(Shelf,null=True,on_delete=models.SET_NULL)
    status= models.CharField(max_length=50,null=True,choices=STATUS)
    image = models.ImageField(upload_to='images/' , default='person.png')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    objects = models.Manager()
    books = BookManager()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-created',)

    def __str__(self):
        return self.title
