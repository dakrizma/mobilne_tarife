from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'', 'j_son.views.input', name='input'),
)