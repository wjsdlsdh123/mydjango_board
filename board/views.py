from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
        return render(request, 'board/index.html',{'athlete_list':['유저', '유저2'], 'athlete_in_locker_room_list': True, })
def bar(request):
        return render(request, 'loo/gar.html')
def gar(request):
        return  render(request, 'loo/gar.html', {'test_list':['bar','gar']})
def tar(request):
        return render(request, 'board/index.html')