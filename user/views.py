from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def django_view(request):
    return HttpResponse("<h1>나의 프로필</h1> <li>이름:전인오</li> <li>별명:inoh </li>")

