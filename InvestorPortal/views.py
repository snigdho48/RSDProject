from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

@login_required(login_url='login')
def p_home(request):
    if request.user.is_authenticated:
        user = request.user
        investor = Investor.objects.all().filter(user=user)
        share = Share.objects.all()
        notice=Notice.objects.all()

        context = {'investor': investor,
                   'share': share,
                   'notice':notice}
    return render(request, 'investor/index.html', context)

@login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        investor = Investor.objects.all().filter(user=user)

        context = {'investor': investor}
    return render(request, 'investor/portfolio.html', context)


@login_required(login_url='login')
def portfolio(request):
    return render(request, 'investor/portfolio.html')


@login_required(login_url='login')
def withdraw(request):
    if request.user.is_authenticated:
        user = request.user
        investor = Investor.objects.all().filter(user=user)

        context = {'investor': investor}
    return render(request, 'investor/withdraw.html', context)


@login_required(login_url='login')
def buy_more(request):
    if request.user.is_authenticated:
        user = request.user
        investor = Investor.objects.all().filter(user=user)

        context = {'investor': investor}
    return render(request, 'investor/buy_more.html',context)


@login_required(login_url='login')
def issue(request):
    if request.user.is_authenticated:
        user = request.user
        investor = Investor.objects.all().filter(user=user)

        context = {'investor': investor}
    return render(request, 'investor/issu.html',context)


@login_required(login_url='login')
def request_buy(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            name = request.POST['name']
            massage = request.POST['message']
            subject = request.POST['subject']
            cell = request.POST['Cell']
            user = request.user
            investor = Investor.objects.get(user=user)
            if email != '' or name != '' or subject != '' or cell != '' or massage != '':
                user = Buy_more.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell,user=investor)
                user.save()

                messages.info(request, "Success")
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.info(request, "Field Can't Be Empty")
                return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def request_withdraw(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            email = request.POST['email']
            name = request.POST['name']
            massage = request.POST['message']
            subject = request.POST['subject']
            cell = request.POST['Cell']
            user = request.user
            investor = Investor.objects.get(user=user)
            if email != '' or name != '' or subject != '' or cell != '' or massage != '':
                user = Withdraw.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell,user=investor)
                user.save()

                messages.info(request, "Success")
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.info(request, "Field Can't Be Empty")
                return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def request_issu(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            email = request.POST['email']
            name = request.POST['name']
            massage = request.POST['message']
            subject = request.POST['subject']
            cell = request.POST['Cell']
            user = request.user
            investor = Investor.objects.get(user=user)
            if email != '' or name != '' or subject != '' or cell != '' or massage != '':
                user = Issue.objects.create(name=name, email=email, message=massage, sub_text=subject, cell=cell,user=investor)
                user.save()

                messages.info(request, "Success")
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.info(request, "Field Can't Be Empty")
                return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.META['HTTP_REFERER'])


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('p_home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('p_home')

            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'investor/login.html', context)


def logutPage(request):
    logout(request)
    return redirect('login')


################# Char View ##################

from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse


def population_chart(request):
    labels = []
    data = []

    queryset = Share_Rate_history.objects.all()
    for entry in queryset:
        labels.append(entry.date)
        data.append(entry.price)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })