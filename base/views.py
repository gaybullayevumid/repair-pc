from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ServicePageView(TemplateView):
    template_name = 'pages/service.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'