from django.shortcuts import render
from django.http import HttpResponse
from django.http import request


# Create your views here.
def homePage(request):
    return  HttpResponse("Hello rasta")
