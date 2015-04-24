from django.conf.urls import patterns, include, url
from django.contrib import admin

# admin.autodiscover()

#TODO: write me (better)!
urlpatterns = patterns('',
    url(r'^$', 'show_example.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
