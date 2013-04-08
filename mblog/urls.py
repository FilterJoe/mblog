from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='home_page'),
    url(r'^blog/', include('blog.urls', namespace='blog')),  # notice the quotes needed around blog.urls
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:  # Needed in order to get Heroku to find CSS. I don't understand why this is needed.
    urlpatterns += patterns('',
                            (r'^static/(.*)$', 'django.views.static.serve', {
                                'document_root': settings.STATIC_ROOT
                            }),
    )
