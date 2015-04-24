from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'show_example.views.home', name='home'),
    url(r'^(?P<article_id>\d+)$', 'show_example.views.home', name='home'),
    url(r'^newperson/$', 'show_example.views.newperson', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
