from django.urls import path

from . import views

urlpatterns=[
    path('',views.django_view, name = "django_view")
]