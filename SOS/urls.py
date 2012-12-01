import os

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': os.path.join(settings.PROJECT_ROOT, 'tiny_mce') }),
)

urlpatterns += patterns('cms.views',
	url(r'^(?P<language>[a-z]{2,3})/(?P<date>\d{4}/[a-z]{3}/\d{2})/(?P<slug>(\w|-)+).html$', 'show_entry'),
	url(r'^(?P<language>[a-z]{2,3})/(?P<slug>(\w|-)+).html$', 'show_page'),
	url(r'^(?P<language>[a-z]{2,3})/$', 'index'),
	url(r'^$', 'index'),
)