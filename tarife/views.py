from tarife.models import Mreza, Racun
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tarife.forms import RacunForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# form.save()
			return render(request, 'tarife/index.html',)
	else:
		form = UserCreationForm()
	return render(request, 'tarife/register.html', {'form': form})

@login_required
def index(request):
	if request.method == 'POST':
		form = RacunForm(request.POST)
		if form.is_valid():
			racun = form.save(commit=False)		# snimi u "clipboard", ali nemoj jos snimiti
			racun.korisnik = request.user		# ovo radimo zato sto moderator je NOT_NULL
			racun.save()						# snimi
			data = []
			json_data = open('remote_server_simulation/data.json')
			data = json.load(json_data)
			br = len(Racun.objects.all())-1

			# i = 0
			# while (i < br):
			# 	if (racun.korisnik == Racun.objects.all()[i].korisnik):
			rn = Racun.objects.all()[br]
			# 	else:
					
			# if korisnik, mjesec, godina:
			# 	unijeli ste podatke za taj mjesec

			mjesec = rn.mjesec
			godina = rn.godina
			korisnik = rn.korisnik
			rez = []
			for x in range(0, len(data)):
				for y in range(0, len(data[x]['tarife'])):
					objects = data[x]['tarife'][y]
					a = izracun(objects, rn.prim, rn.druge, rn.sms, rn.mms, rn.net, x, y)
					if y==0:
						a_min = a
					if a<=a_min:
						a_min = a
						a_rez = format(round(a, 2), '.2f')
						tarifa = data[x]['tarife'][y]['ime_tarife']
				rez.append(data[x]['mreza'])
				rez.append(tarifa)
				rez.append(a_rez)
			len_br = len(data)
			json_data.close()
			return render(request, 'tarife/izracun.html', {'rez': rez, 'len_br': len_br, 'mjesec': mjesec, 'godina': godina, 'korisnik': korisnik})
	else:
		form = RacunForm()
	
	return render(request, 'tarife/index.html', {'form': form})

def izracun(objects, br_prim, br_druge, br_sms, br_mms, br_net, x, y):
	if objects['prim'] + objects['druge'] > 2 and objects['prim'] == objects['druge']:
		if br_prim + br_druge <= objects['prim']:
			prim_sum = 0
			druge_sum = 0
		else:
			druge_sum = prim_sum = (br_prim+br_druge-objects['prim'])*objects['prim_cij']*objects['uspostava']
	else:
		if br_prim <= objects['prim'] or objects['prim'] == 1:
			prim_sum = 0
		else:
			prim_sum = (br_prim-objects['prim'])*objects['prim_cij']*objects['uspostava']
		if br_druge <= objects['druge'] or objects['druge'] == 1:
			druge_sum = 0
		else:
			druge_sum = (br_druge-objects['druge'])*objects['druge_cij']*objects['uspostava']
	if br_sms <= objects['sms'] or objects['sms'] == 1:
		sms_sum = 0
	else:
		sms_sum = (br_sms-objects['sms'])*objects['sms_cij']
	mms_sum = br_mms*objects['mms_cij']
	if br_net <= objects['net'] or objects['net'] == 1:
		net_sum = 0
	else:
		net_sum = (br_net-objects['net'])*objects['net_cij']
	rez = prim_sum + druge_sum + sms_sum + mms_sum + net_sum + objects['pretplata'] + objects['naknada']
	return rez