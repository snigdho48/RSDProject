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
    return render(request, 'about.html')


def News(request):
    return render(request, 'News_and_events.html')


def contact(request):
    return render(request, 'contact.html')


def partnerships(request):
    return render(request, 'partnerships.html')


def products(request):
    return render(request, 'products.html')


def products_details(request):
    return render(request, 'products_details.html')


def event_details(request):
    return render(request, 'Event_details.html')


def contact(request):
    return render(request, 'contact.html')


def handler404(request, exception=None):
    return render(request, '404.html', status=404)


def brands(request):
    return render(request, 'brands.html')


def career(request):
    return render(request, 'career.html')


def testimonial(request):
    return render(request, 'testimonial.html')
