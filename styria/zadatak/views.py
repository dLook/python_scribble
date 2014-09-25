from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from zadatak.models import Url, Words, WordCount
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction

import feedparser
import collections

# Create your views here.
def index(request):
	url_list = Url.objects.all()
	context = {"url_list": url_list}
	return render(request, 'zadatak/index.html', context)

def url_save(request):
	data = Url(url_data=request.POST['url_data'])
	data.save()
	return HttpResponseRedirect(reverse('zadatak:index'))

def url_process(request):
	not_empty = request.POST.getlist('cb')
	for x in Url.objects.all():
		x.status = False
		x.save()
	value = list()
	if request.POST and not_empty:
		for x in range(0, len(not_empty)):
			db_entry = Url.objects.get(pk=not_empty[x])
			db_entry.status = True
			db_entry.save()
			all_words = allWords(db_entry.url_data)
			# dio za spremanje jedinstvene rijeci u bazu
			singleWord(all_words, db_entry.id)
			value.append(db_entry)
		context = {"data": value}
		return render(request, 'zadatak/url_process.html', context)
	else:
		return HttpResponseRedirect(reverse('zadatak:index'))

def details(request, url_id):
	data = WordCount.objects.filter(url_id=url_id).order_by('-total')
	value = Url.objects.get(pk=url_id)
	paginator = Paginator(data, 30)
	page = request.GET.get('page')
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	context = {"data": data, "value": value.url_data}
	#return render(request, 'zadatak/details.html', context)
	return render_to_response('zadatak/details.html', context)

def singleWord(all_words, url_id):
	#for x in Words.objects.all():
	#	x.delete()
	helper = list()
	for x in all_words:
		helper += x
	# odredivanje koliko se puta pojedina rijec pojavljuje
	# ovo je ujedno i dictionary s jedinstvenim rijecima
	word_count = collections.Counter(helper)
	# unique_word je da mogu referencirati dictionary word_count
	unique_word = list(set(helper))
	#sad to treba spremiti u bazu
	# ovaj dio je izuzetno spor, ali kad se ukljuci ovo
	# transaction.atomic() onda se ubrza
	with transaction.atomic():
                for x in word_count:
                        data = Words(url_id=url_id, word=x)
                        data.save()
                        data = WordCount(url_id=url_id, word_id=x, total=word_count.get(x))
                        data.save()
	return ()

def allWords(url):
	d = feedparser.parse(url)
	r_value = list()
	for x in d.entries:
		data = x.description
		text = ''.join(word if word.isalnum() else ' ' for word in data).split()
		# u text varijabli nalaze se sve rijeci za pojedini description
		r_value.append(text)
	#r_value je lista svih rijeci u svim descriptionima pojedinog feeda
	return r_value
