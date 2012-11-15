from django.http import HttpResponse

def index(request, language='az'):
	return HttpResponse('language: %s' % language)

def show_page(request, language, slug):
	return HttpResponse('language: %s, slug: %s' % (
			language, slug
		))

def show_entry(request, language, year, month, day, slug):
	return HttpResponse('language: %s, year: %s, month: %s, day: %s, slug: %s' % (
			language, year, month, day, slug
		))
