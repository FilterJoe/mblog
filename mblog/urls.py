from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import homepage

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', homepage),
    # url(r'^mblog/', include('mblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:  # Needed in order to get Heroku to find CSS. I don't understand why this is needed.
    urlpatterns += patterns('',
                            (r'^static/(.*)$', 'django.views.static.serve', {
                                'document_root': settings.STATIC_ROOT
                            }),
    )
