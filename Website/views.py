from typing import ContextManager
from Website.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic


def home(request):
    data = Contact_Info.objects.all()
    product = Products.objects.all()
    posts = reversed(NewsandEvent.objects.all())
    f_post = reversed(NewsandEvent.objects.all())
    brands = Brands.objects.all()
    banners = Slide_Images.objects.all()
    overview = Company_Overview.objects.all()
    board_of_directors = Board_of_directors.objects.all()
    links = Topbar_footer.objects.all()
    image = Slide_Images.objects.all()
    context = {'data': data,
               'products': product,
               'brands': brands,
               'po': posts,
               'links': links,
               'overview': overview,
               'image': image,
               'board_of_directors': board_of_directors,
               'f_post': f_post,
               'banners': banners,
               }
    return render(request, 'index.html', context)


def about(request):
    posts = reversed(NewsandEvent.objects.all())
    data = Contact_Info.objects.all()
    abouts = About_us.objects.all()
    links = Topbar_footer.objects.all()
    context = {'data': data,
               'abouts': abouts,
               'links': links,
               'po': posts, }
    return render(request, 'about.html', context)


def NewsList(request):
    links = Topbar_footer.objects.all()
    posts = reversed(NewsandEvent.objects.all())
    f_post = reversed(NewsandEvent.objects.all())
    data = Contact_Info.objects.all()
    context = {'data': data,
               'po': posts,
               'links': links,
               'f_post': f_post,
               }

    return render(request, 'News_and_events.html', context)


def NewsDetail(request, slug):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    f_post = reversed(NewsandEvent.objects.all())
    post = NewsandEvent.objects.get(slug=slug)
    data = Contact_Info.objects.all()
    context = {'data': data,
               'post': post,
               'links': links,
               'po': posts,
               'f_post': f_post}
    return render(request, 'Event_details.html', context)


def partnerships(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    partners = Our_partner.objects.all()
    context = {'data': data,
               'partners': partners,
               'links': links,
               'po': posts, }
    return render(request, 'partnerships.html', context)


def products(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    product = Products.objects.all()
    context = {'data': data,
               'product': product,
               'links': links,
               'po': posts, }
    return render(request, 'products.html', context)


def contact(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    contacts = Contact.objects.all()
    context = {'data': data,
               'contact': contacts,
               'links': links,
               'po': posts, }
    return render(request, 'contact.html', context)


def error_404(request, exception=None):
    data = {}
    return render(request, '404.html', data)


def brands(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    brands = Brands.objects.all()
    context = {'data': data,
               'brands': brands,
               'links': links,
               'po': posts, }
    return render(request, 'brands.html', context)


def career(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    careers = Career.objects.all()
    context = {'data': data,
               'career': careers,
               'links': links,
               'po': posts, }
    return render(request, 'career.html', context)


def catalog(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    product = Products.objects.all()
    context = {'products': product,
               'data': data,
               'links': links,
               'po': posts, }
    return render(request, 'catalog.html', context)


def investor_req(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    contacts = Contact.objects.all()
    context = {'data': data,
               'contact': contacts,
               'links': links,
               'po': posts, }
    return render(request, 'investor_request.html', context)

def about_investment(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    contacts = Contact.objects.all()
    about_invest =About_investment.objects.all()
    context = {'data': data,
               'contact': contacts,
               'links': links,
               'about_invest':about_invest,
               'po': posts,}
    return render(request, 'about_investment.html', context)

def investment_policy(request):
    posts = reversed(NewsandEvent.objects.all())
    links = Topbar_footer.objects.all()
    data = Contact_Info.objects.all()
    contacts = Contact.objects.all()
    invest_policy =Investment_policy.objects.all()
    context = {'data': data,
               'contact': contacts,
               'links': links,
               'invest_policy':invest_policy,
               'po': posts}
    return render(request, 'Investment_policy.html', context)


def Subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email != '':
            user = subscribe.objects.create(email=email)
            user.save()
            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Field Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def Subscribe_footer(request):
    if request.method == 'POST':
        email = request.POST['email-f']
        if email != '':
            user = subscribe.objects.create(email=email)
            user.save()
            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Email Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def send_massage(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        massage = request.POST['message']
        subject = request.POST['subject']
        cell = request.POST['Cell']
        if email != '' or name != '' or subject != '' or cell != '' or massage != '':
            user = Contact.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell)
            user.save()
            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Field Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def send_request(request):

    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        massage = request.POST['message']
        subject = request.POST['subject']
        cell = request.POST['Cell']
        if email != '' or name != '' or subject != '' or cell != '' or massage != '':
            user = investor_request.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell)
            user.save()
            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Field Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])
