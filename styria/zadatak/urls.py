from django.conf.urls import patterns, url

from zadatak import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'url_save/$', views.url_save, name='url_save'),
	url(r'url_process/$', views.url_process, name='url_process'),
	url(r'^(?P<url_id>\d+)/$', views.details, name='details'),
	)