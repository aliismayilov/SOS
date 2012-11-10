from django.contrib import admin

from cms.models import *

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Language)
admin.site.register(Page, PageAdmin)
admin.site.register(Entry, EntryAdmin)
