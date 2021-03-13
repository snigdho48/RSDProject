from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *


# Create your views here.


def p_home(request):
    return render(request, 'investor/index.html')


def portfolio(request):
    return render(request, 'investor/portfolio.html')


def withdraw(request):
    return render(request, 'investor/withdraw.html')


def buy_more(request):
    return render(request, 'investor/buy_more.html')


def issue(request):
    return render(request, 'investor/issu.html')


def request_buy(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        massage = request.POST['message']
        subject = request.POST['subject']
        cell = request.POST['Cell']
        if email != '' or name != '' or subject != '' or cell != '' or massage != '':
            user = Buy_more.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell)
            user.save()

            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Field Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def request_withdraw(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        massage = request.POST['message']
        subject = request.POST['subject']
        cell = request.POST['Cell']
        if email != '' or name != '' or subject != '' or cell != '' or massage != '':
            user = Withdraw.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell)
            user.save()

            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Field Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])


def request_issu(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        massage = request.POST['message']
        subject = request.POST['subject']
        cell = request.POST['Cell']
        if email != '' or name != '' or subject != '' or cell != '' or massage != '':
            user = Issue.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell)
            user.save()

            messages.info(request, "Success")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request, "Field Can't Be Empty")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])
