from django.urls import path

from . import views


urlpatterns = [

        path('', views.home, name='home'),
        path('event_details/', views.event_details, name='event_details'),
        path('products/', views.products, name='products'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('partnerships/', views.partnerships, name='partnerships'),
        path('brands/', views.brands, name='brands'),
        path('career/', views.career, name='career'),
        path('catalog/',views.catalog,name='catalog'),
        path('NewsList/', views.NewsList, name='NewsList'),
        path('<slug:slug>/', views.NewsDetail, name='News_detail'),
]
