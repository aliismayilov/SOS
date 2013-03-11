from django.contrib import admin
from django.conf import settings

from cms.models import *

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_filter = ('language',)
	class Media:
		js = (settings.STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce_src.js',
			  settings.STATIC_URL + 'filebrowser/js/TinyMCEAdmin.js',)

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_filter = ('language',)
	class Media:
		js = (settings.STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce_src.js',
			  settings.STATIC_URL + 'filebrowser/js/TinyMCEAdmin.js',)

admin.site.register(Language)
admin.site.register(Page, PageAdmin)
admin.site.register(Entry, EntryAdmin)
