import os

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('cms.views',
	url(r'^(?P<language>[a-z]{2,3})/news/(?P<date>\d{4}/[a-z]{3}/\d{2})/(?P<slug>(\w|-)+).html$', 'show_entry'),
	url(r'^(?P<language>[a-z]{2,3})/news/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive'),
	url(r'^(?P<language>[a-z]{2,3})/news/(?P<year>\d{4})/$', 'archive'),
	url(r'^(?P<language>[a-z]{2,3})/news/$', 'archive'),
	url(r'^(?P<language>[a-z]{2,3})/search$', 'search'),
	url(r'^(?P<language>[a-z]{2,3})/(?P<slug>(\w|-)+).html$', 'show_page'),
	url(r'^(?P<language>[a-z]{2,3})/$', 'index'),
	url(r'^$', 'index'),
)