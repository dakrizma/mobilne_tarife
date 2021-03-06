# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

class Mreza(models.Model):
	ime_mreze = models.CharField(max_length=50)

	def __str__(self):
		return self.ime_mreze

	class Meta:
		verbose_name_plural = 'mreze'

year_dropdown = []
for y in range(2010, (datetime.datetime.now().year)+1):
	year_dropdown.append((y, y))

month_dropdown = (
	(u'siječanj', u'siječanj'),
	(u'veljača', u'veljača'),
	(u'ožujak', u'ožujak'),
	(u'travanj', u'travanj'),
	(u'svibanj', u'svibanj'),
	(u'lipanj', u'lipanj'),
	(u'srpanj', u'srpanj'),
	(u'kolovoz', u'kolovoz'),
	(u'rujan', u'rujan'),
	(u'listopad', u'listopad'),
	(u'studeni', u'studeni'),
	(u'prosinac', u'prosinac'),
	)

class Racun(models.Model):
	prim = models.IntegerField()
	druge = models.IntegerField()
	sms = models.IntegerField()
	mms = models.IntegerField()
	net = models.IntegerField()
	mjesec = models.CharField(max_length=8, choices=month_dropdown,)
	godina = models.IntegerField(('godina'), max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)
	korisnik = models.ForeignKey(User, )

	class Meta:
		verbose_name_plural = 'racuni'