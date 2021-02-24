from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def Index(request):
    return HttpResponse("hello")