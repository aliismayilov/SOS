from django.contrib import admin
from django.conf import settings

from cms.models import *

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_filter = ('language',)
	class Media:
		js = (settings.STATIC_URL + 'tiny_mce/tiny_mce.js',
			  settings.STATIC_URL + 'js/tiny_mce_init.js',)

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_filter = ('language',)
	class Media:
		js = (settings.STATIC_URL + 'tiny_mce/tiny_mce.js',
			  settings.STATIC_URL + 'js/tiny_mce_init.js',)

admin.site.register(Language)
admin.site.register(Page, PageAdmin)
admin.site.register(Entry, EntryAdmin)
