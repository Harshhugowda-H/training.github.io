from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('testimonials',views.testimonials,name='testimonials'),
    path('whatsapp',views.whatsapp,name='whatsapp'),
    path('responseList',views.responseList,name='responseList'),
    path('deleteData',views.deleteData,name='deleteData'),
    path('sort',views.sort,name='sort'),
    path('search',views.search,name='search')
]
