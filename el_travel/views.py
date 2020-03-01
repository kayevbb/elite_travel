from django.shortcuts import render
from .models import Pole
from django.views.generic import ListView
# Create your views here.

class IndexView(ListView):
    model = Pole
    template_name = 'index.html'

    def get_queryset(self):
        return Pole.objects.exclude(status=False)


class AboutView(ListView):
    model = Pole
    template_name = 'about.html'


class BlogView(ListView):
    model = Pole
    template_name = 'blog.html'


class BlogSingleView(ListView):
    model = Pole
    template_name = 'blog-single.html'


class ContactView(ListView):
    model = Pole
    template_name = 'contact.html'


class DestinationView(ListView):
    model = Pole
    template_name = 'destination.html'


class HotelView(ListView):
    model = Pole
    template_name = 'hotel-resto.html'

