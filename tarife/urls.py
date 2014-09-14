# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^register/$', 'tarife.views.register', name='register'),
	url(r'^izracun/$', 'tarife.views.izracun', name='izracun'),
	url(r'^brisanje/$', 'tarife.views.brisanje', name='brisanje'),
	url(r'^$', 'tarife.views.index', name='index'),
)