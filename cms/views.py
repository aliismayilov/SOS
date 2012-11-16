from cms.models import Language, Page

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

def index(request, language='az'):
	return HttpResponse('language: %s' % language)

def show_page(request, language, slug):
	language = get_object_or_404(Language, small_name=language)
	page = get_object_or_404(Page, slug=slug, language=language)

	return render_to_response('show_page.html', {'page': page})

def show_entry(request, language, year, month, day, slug):
	return HttpResponse('language: %s, year: %s, month: %s, day: %s, slug: %s' % (
			language, year, month, day, slug
		))
