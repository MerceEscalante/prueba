from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Singup.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', 'Singup.views.thankyou', name='thankyou'),
    url(r'^productos/$', 'Singup.views.productos', name='productos'),
    url(r'^about-us/$', 'Singup.views.aboutus', name='aboutus'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    