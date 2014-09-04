from tarife.models import Mreza, Tarifa
from tarife.forms import RacunForm
from django.shortcuts import render
import json

def index(request):
	if request.method == 'POST':
		form = RacunForm(request.POST)
		if form.is_valid():
			mreza = form.cleaned_data['mreza']
			prim = form.cleaned_data['prim']
			druge = form.cleaned_data['druge']
			sms = form.cleaned_data['sms']
			mms = form.cleaned_data['mms']
			net = form.cleaned_data['net']
			rez = []
			for x in range(0, len(Mreza.objects.all())):
				a_min = 99999
				for y in range(0, len(Tarifa.objects.all())):
					if (Tarifa.objects.all()[y].mreza == Mreza.objects.all()[x]):
						a = izracun(prim, druge, sms, mms, net, y)
						if a<a_min:
							a_min = format(round(a, 2), '.2f')
							tarifa = Tarifa.objects.all()[y].ime_tarife
				rez.append(Mreza.objects.all()[x].ime_mreze)
				rez.append(tarifa)
				rez.append(a_min)
			len_br = len(Tarifa.objects.all())
			return render(request, 'tarife/izracun.html', {'rez': rez, 'len_br': len_br})
	else:
		form = RacunForm()
		return render(request, 'tarife/index.html', {'form': form})

def izracun(br_prim, br_druge, br_sms, br_mms, br_net, br):
	objects = Tarifa.objects.all()[br]
	if objects.prim + objects.druge > 2 and objects.prim == objects.druge:
		if br_prim + br_druge <= objects.prim:
			prim_sum = 0
			druge_sum = 0
		else:
			druge_sum = prim_sum = (br_prim+br_druge-objects.prim)*(objects.prim_cij)*(objects.uspostava)
	else:
		if br_prim <= objects.prim or objects.prim == 1:
			prim_sum = 0
		else:
			prim_sum = (br_prim-objects.prim)*(objects.prim_cij)*(objects.uspostava)
		if br_druge <= objects.druge or objects.druge == 1:
			druge_sum = 0
		else:
			druge_sum = (br_druge-objects.druge)*(objects.druge_cij)*(objects.uspostava)
	if br_sms <= objects.sms or objects.sms == 1:
		sms_sum = 0
	else:
		sms_sum = (br_sms-objects.sms)*(objects.sms_cij)
	if br_mms <= objects.mms or objects.mms == 1:
		mms_sum = 0
	else:
		mms_sum = (br_mms-objects.mms)*(objects.mms_cij)
	if br_net <= objects.net or objects.net == 1:
		net_sum = 0
	else:
		net_sum = (br_net-objects.net)*(objects.net_cij)
	rez = prim_sum + druge_sum + sms_sum + mms_sum + net_sum + objects.pretplata + objects.naknada
	return rez