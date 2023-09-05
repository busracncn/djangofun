from django.urls import path

from . import views

urlpatterns = [
    path("hogwarts", views.index, name="index"),
]