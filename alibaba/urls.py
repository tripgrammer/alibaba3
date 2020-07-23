
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('hotel.urls')),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('login/static', document_root=settings.STATIC_ROOT)

