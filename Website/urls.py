from django.urls import path, include

import Website
from . import views


urlpatterns = [

        path('', views.home, name='home'),
        path('subscribe/',views.Subscribe,name='Subscribe'),
        path('request/',views.investor_req,name='investor_req'),
        path('investor-request/',views.send_request,name='send_request'),
        path('send_massage/',views.send_massage,name='send_massage'),
        path('subscribes/',views.Subscribe_footer,name='Subscribe_footer'),
        path('products/', views.products, name='products'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('partnerships/', views.partnerships, name='partnerships'),
        path('brands/', views.brands, name='brands'),
        path('career/', views.career, name='career'),
        path('catalog/',views.catalog,name='catalog'),
        path('NewsList/', views.NewsList, name='NewsList'),
        path('about_investment/', views.about_investment, name='about_investment'),
        path('investment_policy/', views.investment_policy, name='investment_policy'),
        path('<slug:slug>/', views.NewsDetail, name='News_detail'),


]

handler404 = Website.views.error_404
handler500 = Website.views.error_404

