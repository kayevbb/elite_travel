from django.urls import path
from .views import (
    IndexView,
    AboutView,
    BlogView,
    BlogSingleView,
    ContactView,
    DestinationView,
    HotelView,

)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-single/', BlogSingleView.as_view(), name='blog-single'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('hotel/', HotelView.as_view(), name='hotel'),
    path('destination/', DestinationView.as_view(), name='destination'),

]
