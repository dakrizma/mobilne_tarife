# -*- coding: utf-8 -*-

from django.forms import ModelForm, ModelChoiceField
from django import forms
from tarife.models import Racun
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse

class RacunForm(ModelForm):
    class Meta:
        model = Racun
        labels = {
			'prim': _(u'Pozivi prema primarnoj mreži u minutama'),
			'druge': _(u'Pozivi prema drugim mrežama u minutama'),
			'sms': _('Broj poslanih sms-ova'),
			'mms': _('Broj poslanih mms-ova'),
			'net': _(u'Količina potrošenog prometa u MB'),
			'mjesec': _(u'Mjesec računa'),
			'godina': _(u'Godina računa'),
			}
        exclude = ('korisnik',)

# class polje_godina(ModelChoiceField):
# 	def label_from_instance(self, obj):
# 		return obj.godina

# class polje_mjesec(ModelChoiceField):
# 	def label_from_instance(self, obj):
# 		return obj.mjesec

# class BrisanjeForm(forms.Form):

# 	# mjesec = forms.CharField(label='mjesec', max_length=10)
# 	# godina = forms.IntegerField(label='godina')

# 	# korisnik1 = forms.ModelForeignKey(Racun.objects.all())
# 	# korisnik2 = forms.ModelChoiceField(queryset=Racun.objects.values_list('korisnik'))
	
# 	# mjesec = polje_mjesec(queryset=Racun.objects.all())
# 	# godina = polje_godina(queryset=Racun.objects.all())

	# mjesec = forms.ModelChoiceField(queryset=Racun.objects.values_list('mjesec'))
	# godina = forms.ModelChoiceField(queryset=Racun.objects.values_list('godina'))
	# godina = polje_godina(queryset=Racun.objects.all())



class BrisanjeForm(ModelForm):
    class Meta:
        model = Racun
        labels = {
			'mjesec': _(u'Mjesec računa'),
			'godina': _(u'Godina računa'),
			}
        exclude = ('korisnik', 'prim', 'druge', 'sms', 'mms', 'net')