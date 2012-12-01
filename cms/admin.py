from django.contrib import admin

from cms.models import *

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	class Media:
		js = ('http://localhost:8000/tiny_mce/tiny_mce.js',
			  'https://s3-eu-west-1.amazonaws.com/soschildrenaz/js/tiny_mce_init.js',)

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	class Media:
		js = ('http://localhost:8000/tiny_mce/tiny_mce.js',
			  'https://s3-eu-west-1.amazonaws.com/soschildrenaz/js/tiny_mce_init.js',)

admin.site.register(Language)
admin.site.register(Page, PageAdmin)
admin.site.register(Entry, EntryAdmin)
