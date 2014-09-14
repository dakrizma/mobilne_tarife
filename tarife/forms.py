# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from tarife.models import *
from django.utils.translation import ugettext_lazy as _

class RacunForm(ModelForm):
    class Meta:
        model = Racun
        labels = {
			'prim': _(u'Pozivi prema primarnoj mreži u minutama'),
			'druge': _(u'Pozivi prema drugim mrežama u minutama'),
			'sms': _(u'Broj poslanih sms-ova'),
			'mms': _(u'Broj poslanih mms-ova'),
			'net': _(u'Količina potrošenog prometa u MB'),
			'mjesec': _(u'Mjesec računa'),
			'godina': _(u'Godina računa'),
			}
        exclude = ('korisnik',)

class BrisanjeForm(ModelForm):
    class Meta:
        model = Racun
        labels = {
			'mjesec': _(u'Mjesec računa'),
			'godina': _(u'Godina računa'),
			}
        exclude = ('korisnik', 'prim', 'druge', 'sms', 'mms', 'net')