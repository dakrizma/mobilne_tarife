from django.db import models
	
class Mreza(models.Model):
	ime_mreze = models.CharField(max_length=50)

	def __str__(self):
		return self.ime_mreze

	class Meta:
		verbose_name_plural = 'mreze'

class Tarifa(models.Model):
	ime_tarife = models.CharField(max_length=100)
	prim_cij = models.DecimalField(max_digits=5, decimal_places=2)
	druge_cij = models.DecimalField(max_digits=5, decimal_places=2)
	sms_cij = models.DecimalField(max_digits=5, decimal_places=2)
	mms_cij = models.DecimalField(max_digits=5, decimal_places=2)
	net_cij = models.DecimalField(max_digits=5, decimal_places=2)
	prim = models.IntegerField(default=1)
	druge = models.IntegerField(default=1)
	sms = models.IntegerField(default=1)
	mms = models.IntegerField(default=1)
	net = models.IntegerField(default=1)
	uspostava = models.DecimalField(max_digits=5, decimal_places=2)
	naknada = models.DecimalField(max_digits=5, decimal_places=2)
	pretplata = models.DecimalField(max_digits=5, decimal_places=2)
	mreza = models.ForeignKey('Mreza')

	def __str__(self):
		return self.ime_tarife

	class Meta:
		verbose_name_plural = 'tarife'