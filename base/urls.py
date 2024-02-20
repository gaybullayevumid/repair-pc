from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('blog', BlogPageView.as_view(), name='blog'),
]
