from django.urls import path

from .views import MainPage, GryffindorPage, SlytherinPage, HufflepuffPage, RavenclawPage

urlpatterns = [
    path("", MainPage.as_view(), name='main'),
    path("gryffindor", GryffindorPage.as_view(), name='gryffindor'),
    path("slytherin", SlytherinPage.as_view(), name='slytherin'),
    path("hufflepuff", HufflepuffPage.as_view(), name='hufflepuff'),
    path("ravenclaw", RavenclawPage.as_view(), name='ravenclaw'),
]