from tarife.forms import RacunForm
from tarife.models import Mreza, Racun
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import json

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# user = request.user
			# user.groups.add('korisnici')
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'tarife/register.html', {'form': form})

@login_required
def index(request):
	if request.method == 'POST':
		form = RacunForm(request.POST)
		if form.is_valid():
			mjesec = form.cleaned_data['mjesec']
			godina = form.cleaned_data['godina']
			k = 0
			greska = []
			objects = Racun.objects.all()
			br = len(objects)
			while (k < br):
				if (mjesec == objects[k].mjesec) and (godina == objects[k].godina) and (request.user == objects[k].korisnik):
					greska.append('Unijeli ste podatke za taj mjesec. Za promjenu podataka kliknite na Promijena podataka ili nastavite sa unosom novog racuna')
					form = RacunForm()
					return render(request, 'tarife/index.html', {'form': form, 'greska': greska})
				k += 1
			racun = form.save(commit=False)
			racun.korisnik = request.user
			racun.save()
			korisnik = request.user
			rez, rez_mjesec, rez_mreza, len_br, br_racuna = izlaz(korisnik)
			return render(request, 'tarife/izracun.html', {'rez': rez, 'rez_mjesec': rez_mjesec, 'rez_mreza': rez_mreza, 'len_br': len_br, 'br_racuna': br_racuna, 'korisnik': korisnik})
	else:
		form = RacunForm()
	return render(request, 'tarife/index.html', {'form': form})

@login_required
def izracun(request):
	objects = Racun.objects.all()
	br = len(objects)
	korisnik = request.user
	i = 0
	postoji = 0
	while (i < br):
		if (korisnik == objects[i].korisnik):
			postoji = 1
		i += 1
	if (postoji):
		rez, rez_mjesec, rez_mreza, len_br, br_racuna = izlaz(korisnik)
		return render(request, 'tarife/izracun.html', {'rez': rez, 'rez_mjesec': rez_mjesec, 'rez_mreza': rez_mreza, 'len_br': len_br, 'br_racuna': br_racuna, 'korisnik': korisnik})
	else:
		form = RacunForm()
		greska = []
		greska.append('ne postoji ni jedan unos!')
		return render(request, 'tarife/index.html', {'form': form, 'greska': greska})

def izracun2(objects, br_prim, br_druge, br_sms, br_mms, br_net, x, y):
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

def izlaz(korisnik):
	data = []
	json_data = open('remote_server_simulation/data.json')
	data = json.load(json_data)
	objects = Racun.objects.all()
	br = len(objects)
	i = j = br_racuna = len_broj = 0
	rez = []
	rez_temp4 = []
	rez_mreza = []
	rez_mjesec = []
	rez_temp3 = []
	while (i < br):
		if (korisnik == objects[i].korisnik):
			rn = objects[i]
			rez_temp = (objects[i].mjesec, objects[i].godina)
			rez_mjesec.append(rez_temp)
			for x in range(0, len(data)):
				for y in range(0, len(data[x]['tarife'])):
					objects2 = data[x]['tarife'][y]
					a = izracun2(objects2, rn.prim, rn.druge, rn.sms, rn.mms, rn.net, x, y)
					b = format(round(a, 2), '.2f')
					b_tarifa = data[x]['tarife'][y]['ime_tarife']
					rez_mreza.append(data[x]['mreza'])
					rez_temp2 = (b_tarifa, b)
					rez_temp3.append(rez_temp2)
					len_broj += 1
				rez_temp4.append((rez_temp3))
				rez_temp3 = []
			rez.append((rez_temp4))
			rez_temp4 = []
			br_racuna += 1
		i += 1
	len_br = (len(data)+1)*3
	json_data.close()
	return (rez, rez_mjesec, rez_mreza, len_br, br_racuna)