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

month_dropdown = []
for m in range(1, 13):
	month_dropdown.append((m, m))

class Racun(models.Model):
	prim = models.IntegerField()
	druge = models.IntegerField()
	sms = models.IntegerField()
	mms = models.IntegerField()
	net = models.IntegerField()
	mjesec = models.IntegerField(('mjesec'), max_length=2, choices=month_dropdown, default=datetime.datetime.now().month)
	godina = models.IntegerField(('godina'), max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)
	korisnik = models.ForeignKey(User)
	mreza = models.ForeignKey('Mreza')

	class Meta:
		verbose_name_plural = 'racuni'