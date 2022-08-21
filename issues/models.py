from ast import arg
from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

from library.models import Book


class Issue(models.Model):

    slug = models.SlugField(max_length=255)
    book= models.ForeignKey(Book,null=True,on_delete=models.SET_NULL)
    username= models.ForeignKey(User,null=True,on_delete=models.SET_NULL)    
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    to_date = models.DateField()
    

    class Meta:
        verbose_name_plural = 'Issues'
        ordering = ('-created',)

    def __str__(self):
        return self.username.username
