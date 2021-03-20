from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Share)
class  InvestorAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','total_invest','own_share','available_amount']
admin.site.register(Investor,InvestorAdmin)
admin.site.register(Notice)
class  IssuAdmin(admin.ModelAdmin):
    list_display = ['user','email','created_at']
admin.site.register(Issue,IssuAdmin)
class  WithdrawAdmin(admin.ModelAdmin):
    list_display = ['user','email','created_at']
admin.site.register(Withdraw,WithdrawAdmin)
class  Buy_moreAdmin(admin.ModelAdmin):
    list_display = ['user','email','created_at']
admin.site.register(Buy_more,Buy_moreAdmin)
admin.site.register(Share_Rate_history)