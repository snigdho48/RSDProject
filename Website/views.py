from typing import ContextManager
from Website.models import Contact_Info, Products, Brands, Board_of_directors
from django.shortcuts import render


def home(request):
    data = Contact_Info.objects.all()
    product = Products.objects.all()
    brands = Brands.objects.all()
    board_of_directors = Board_of_directors.objects.all()
    context = {'data': data,
               'products': product,
               'brands': brands,
               'board_of_directors': board_of_directors}
    return render(request, 'index.html', context)


def about(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'about.html',context)


def News(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'News_and_events.html',context)





def partnerships(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'partnerships.html',context)


def products(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'products.html',context)


def products_details(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'products_details.html',context)


def event_details(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'Event_details.html',context)


def contact(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'contact.html',context)


def handler404(request, exception=None):
    return render(request, '404.html', status=404)


def brands(request):
    data = Contact_Info.objects.all()
    context = {'data': data,}
    return render(request, 'brands.html',context)


def career(request):
    data = Contact_Info.objects.all()
    context={'data': data,}
    return render(request, 'career.html',context)


def testimonial(request):
    data = Contact_Info.objects.all()
    context={'data': data,}
    return render(request, 'testimonial.html',context)

def catalog(request):
    data = Contact_Info.objects.all()
    product = Products.objects.all()
    context={'products': product,
             'data':data}
    return render(request,'catalog.html',context)
