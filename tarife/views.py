# -*- coding: utf-8 -*-
from tarife.forms import RacunForm, BrisanjeForm
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
			objects = Racun.objects.all()
			br = len(objects)
			while (k < br):
				if (mjesec == objects[k].mjesec) and (godina == objects[k].godina) and (request.user == objects[k].korisnik):
					greska = 'Unijeli ste podatke za taj mjesec. Za brisanje računa kliknite na \'brisanje računa\' ili nastavite sa unosom novog računa'
					form = RacunForm()
					return render(request, 'tarife/index.html', {'form': form, 'greska': greska})
				k += 1
			racun = form.save(commit=False)
			racun.korisnik = request.user
			racun.save()
			korisnik = request.user
			rez, rez_mjesec = izlaz(korisnik)
			return render(request, 'tarife/izracun.html', {'rez': rez, 'rez_mjesec': rez_mjesec})
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
		rez, rez_mjesec = izlaz(korisnik)
		return render(request, 'tarife/izracun.html', {'rez': rez, 'rez_mjesec': rez_mjesec})
	else:
		form = RacunForm()
		greska = []
		greska.append('ne postoji ni jedan unos!')
		return render(request, 'tarife/index.html', {'form': form, 'greska': greska})

@login_required
def brisanje(request):
	if request.method == 'POST':
		form = BrisanjeForm(request.POST)
		if form.is_valid():
			# form.fields['mjesec'].queryset = Racun.objects.filter(korisnik=request.user)
			# form.fields['godina'].queryset = Racun.objects.filter(korisnik=request.user)
			mjesec = form['mjesec'].value()
			god = form['godina'].value()
			godina = int(god)
			k = 0
			objects = Racun.objects.all()
			br = len(objects)
			while (k < br):
				form = BrisanjeForm()
				if (mjesec == objects[k].mjesec) and (godina == objects[k].godina) and (request.user == objects[k].korisnik):
					objects[k].delete()
					poruka = 'Račun obrisan!'
					return render(request, 'tarife/brisanje.html', {'form': form, 'poruka': poruka})
				else:
					poruka = 'Pokušavate obrisati nepostojeći račun'
				k += 1
			return render(request, 'tarife/brisanje.html', {'form': form, 'poruka': poruka})
	else:
		form = BrisanjeForm()
	return render(request, 'tarife/brisanje.html', {'form': form})

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
	json_data = open('remote_server_simulation/data.json')		# treba staviti exeption ako ne postoji
	data = json.load(json_data)
	objects = Racun.objects.all()
	br = len(objects)
	i = j = 0
	rez = []
	rez_temp4 = []
	rez_mjesec3 = []
	rez_temp3 = []
	rez_temp33 = []
	rez2 = []
	while (i < br):
		if (korisnik == objects[i].korisnik):
			rn = objects[i]
			rez_mjesec2 = mj_god(rn.mjesec, rn.godina)
			rez_temp = (rn.mjesec, rn.godina, rez_mjesec2)
			rez_mjesec3.append(rez_temp)
			rez_temp4 = [rez_mjesec2]
			rez_mjesec = []
			for x in range(0, len(data)):
				for y in range(0, len(data[x]['tarife'])):
					objects2 = data[x]['tarife'][y]
					a = izracun2(objects2, rn.prim, rn.druge, rn.sms, rn.mms, rn.net, x, y)
					a_tarifa = data[x]['tarife'][y]['ime_tarife']
					rez_mreza = (data[x]['mreza'])
					rez_temp2 = (rez_mreza, a_tarifa, a)
					rez_temp3.append(rez_temp2)
				rez_temp33 = sorted(rez_temp3, key=lambda cijena: cijena[2], reverse=True)
				rez_temp4.append(rez_temp33)
				rez_temp33 = []
				rez_temp3 = []
			rez.append(rez_temp4)
			rez_temp4 = []
		i += 1
	rez2 = sorted(rez, key=lambda mj_gd: mj_gd[0])
	for x in range(0, len(rez2)):
		del rez2[x][0]
	rez_mjesec = sorted(rez_mjesec3, key=lambda mj_god: mj_god[2])
	json_data.close()
	return (rez2, rez_mjesec)

def mj_god(mjesec, godina):
	god = mj = 0
	god = int(godina) * 100
	if (mjesec == u'siječanj'):
		mj = 1
	if (mjesec == u'veljača'):
		mj = 2
	if (mjesec == u'ožujak'):
		mj = 3
	if (mjesec == 'travanj'):
		mj = 4
	if (mjesec == 'svibanj'):
		mj = 5
	if (mjesec == 'lipanj'):
		mj = 6
	if (mjesec == 'srpanj'):
		mj = 7
	if (mjesec == 'kolovoz'):
		mj = 8
	if (mjesec == 'rujan'):
		mj = 9
	if (mjesec == 'listopad'):
		mj = 10
	if (mjesec == 'studeni'):
		mj = 11
	if (mjesec == 'prosinac'):
		mj = 12
	return(god + mj)
