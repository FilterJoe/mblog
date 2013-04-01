from django.conf.urls import patterns, include, url
from blog.views import homepage
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', homepage),
    # url(r'^mblog/', include('mblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r"^$", TemplateView.as_view(template_name="index.html")),   # quick hack to get things going
    url(r'^admin/', include(admin.site.urls)),
)
