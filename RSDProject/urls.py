from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="RS Meena Admin Panel"
admin.site.site_title="Welcome To RS Meena Admin Portal!"
admin.site.index_title="Welcome To RS Meena Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Website.urls'))
    #url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
