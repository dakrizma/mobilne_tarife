from django.forms import ModelForm
from tarife.models import Mreza
from django.db import models
from django import forms

class RacunForm(forms.Form):
	mreza = forms.ModelChoiceField(queryset=Mreza.objects.all())
	prim = forms.IntegerField(min_value=0)
	druge = forms.IntegerField(min_value=0)
	sms = forms.IntegerField(min_value=0)
	mms = forms.IntegerField(min_value=0)
	net = forms.IntegerField(min_value=0)