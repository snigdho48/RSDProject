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
]

# handler404 = Website.views.error_404
# handler500 = Website.views.error_404

