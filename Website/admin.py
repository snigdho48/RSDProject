from django.contrib import admin
from Website.models import *
# Register your models here.

admin.site.register(Contact_Info)
admin.site.register(Slide_Images)
admin.site.register(Brands)
admin.site.register(Topbar_footer)
class Company_OverviewAdmin(admin.ModelAdmin):
    list_display = ['total_products', 'active_employees', 'active_dealers','total_brands']
admin.site.register(Company_Overview,Company_OverviewAdmin)
admin.site.register(Products)
admin.site.register(Board_of_directors)
admin.site.register(Our_partner)
admin.site.register(subscribe)
admin.site.register(NewsandEvent)
admin.site.register(About_us)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'cell','created_at']
admin.site.register(Contact,ContactAdmin)
admin.site.register(Career)
admin.site.register(Investment_policy),
admin.site.register(About_investment),
admin.site.register(investor_request)