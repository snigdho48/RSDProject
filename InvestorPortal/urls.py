from django.urls import path

from . import views


urlpatterns = [

        path('dashboard/', views.p_home, name='p_home'),
        path('profile/', views.portfolio, name='portfolio'),
        path('withdraw/', views.withdraw, name='withdraw'),
        path('buy/', views.buy_more, name='buy_more'),
        path('req_issue/', views.request_issu, name='request_issue'),
        path('issue/', views.issue, name='issue'),
        path('buy_req/', views.request_buy, name='request_buy'),
        path('withdraw_req/', views.request_withdraw, name='request_withdraw'),
        path('login/', views.loginPage , name='login'),
        path('logout/', views.logutPage , name='logout'),
       # path('price-chart/', views.price_chart, name='price-chart'),
       path('population-chart/', views.population_chart, name='population-chart'),

]


