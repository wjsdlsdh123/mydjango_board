from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('1',views.bar, name= "bar" ),
    path('2',views.gar, name= "gar"),
    path('3',views.tar, name= "tar"),
]