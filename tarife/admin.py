# -*- coding: utf-8 -*-

from django.contrib import admin
from tarife.models import *

class MrezaAdmin(admin.ModelAdmin):
	list_display = ('id', 'ime_mreze')

class RacunAdmin(admin.ModelAdmin):
	list_display = ('id', 'mjesec', 'godina', 'prim', 'druge', 'sms', 'mms', 'net', 'korisnik')
	list_filter = ('korisnik',)

admin.site.register(Mreza, MrezaAdmin)
admin.site.register(Racun, RacunAdmin)