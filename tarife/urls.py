from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'tarife.views.index', name='index'),
)