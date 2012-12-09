from datetime import datetime

from cms.models import Language, Page, Entry

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def index(request, language='az'):
	language = get_object_or_404(Language, small_name=language)

	return render_to_response('index.html', {
				'current_language': language,
				'languages': Language.objects.all(),
				'top_links': Page.objects.filter(language=language, parent=None)[:5],
				'bottom_links': Page.objects.filter(language=language, parent=None)[5:8],
				'side_links': Page.objects.filter(language=language, parent=None)[8:],
				'latest_entries': Entry.objects.filter(language=language).exclude(image=None)[:3],
			},
		context_instance=RequestContext(request))

def show_page(request, language, slug):
	language = get_object_or_404(Language, small_name=language)
	page = get_object_or_404(Page, slug=slug, language=language)

	return render_to_response('show_page.html', {
				'current_language': language,
				'languages': Language.objects.all(),
				'top_links': Page.objects.filter(language=language, parent=None)[:5],
				'bottom_links': Page.objects.filter(language=language, parent=None)[5:8],
				'side_links': Page.objects.filter(language=language, parent=None)[8:],
				'latest_entries': Entry.objects.filter(language=language).exclude(image=None)[:3],
				'page': page,
			},
		context_instance=RequestContext(request))

def show_entry(request, language, date, slug):
	language = get_object_or_404(Language, small_name=language)
	date = datetime.strptime(date, "%Y/%b/%d")

	entry = get_object_or_404(Entry,
			language=language,
			date_published__year=date.year,
			date_published__month=date.month,
			date_published__day=date.day,
			slug=slug
		)

	return render_to_response('show_entry.html', {
				'current_language': language,
				'languages': Language.objects.all(),
				'top_links': Page.objects.filter(language=language, parent=None)[:5],
				'bottom_links': Page.objects.filter(language=language, parent=None)[5:8],
				'side_links': Page.objects.filter(language=language, parent=None)[8:],
				'latest_entries': Entry.objects.filter(language=language).exclude(image=None)[:3],
				'entry': entry,
			},
		context_instance=RequestContext(request))

def archive(request, language, year, month=None):
	language = get_object_or_404(Language, small_name=language)
	
	if month:
		date = datetime.strptime(year + "/" + month, "%Y/%b")
		entries = Entry.objects.filter(
				language=language,
				date_published__year=date.year,
				date_published__month=date.month,
			)
	else:
		date = datetime.strptime(year, "%Y")
		entries = Entry.objects.filter(
				language=language,
				date_published__year=date.year,
			)

	return render_to_response('archive.html', {
				'current_language': language,
				'languages': Language.objects.all(),
				'top_links': Page.objects.filter(language=language, parent=None)[:5],
				'bottom_links': Page.objects.filter(language=language, parent=None)[5:8],
				'side_links': Page.objects.filter(language=language, parent=None)[8:],
				'entries': entries,
				'year': date.year,
				'month': date.strftime("%B") if month else '',
			},
		context_instance=RequestContext(request))
