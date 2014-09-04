from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^register/$', 'tarife.views.register', name='register'),
	url(r'^izracun/$', 'tarife.views.izracun', name='izracun'),
	url(r'^$', 'tarife.views.index', name='index'),
)