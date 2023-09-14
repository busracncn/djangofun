from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# Create your views here.


class MainPage(View):
    template_name = "main.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class GryffindorPage(View):
    template_name = "house_base.html"

    def get(self, request, *args, **kwargs):
        context = {
            'common_room_img': 'image/gryffindor-common-room.png',
            'house': 'Gryffindor'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class SlytherinPage(View):
    template_name = "house_base.html"

    def get(self, request, *args, **kwargs):
        context = {
            'common_room_img': 'image/slytherin-common-room.png',
            'house': 'Slythrein'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class HufflepuffPage(View):
    template_name = "house_base.html"

    def get(self, request, *args, **kwargs):
        context = {
            'common_room_img': 'image/hufflepuff-common-room.png',
            'house': 'Hufflepuff'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class RavenclawPage(View):
    template_name = "house_base.html"

    def get(self, request, *args, **kwargs):
        context = {
            'common_room_img': 'image/ravenclaw-common-room.png',
            'house': 'Ravenclaw'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)