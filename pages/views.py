from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def PageView(request):
    return HttpResponse("Hello, World!")

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutViewPage(TemplateView):
    template_name = 'about.html'

