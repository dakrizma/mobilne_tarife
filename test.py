import json
# from tarife.models import Mreza, Racun

def izracun(br_prim, br_druge, br_sms, br_mms, br_net, x, y):
	objects = data[x]['tarife'][y]
	if objects['prim'] + objects['druge'] > 2 and objects['prim'] == objects['druge']:
		if br_prim + br_druge <= objects['prim']:
			prim_sum = 0
			druge_sum = 0
		else:
			druge_sum = prim_sum = (br_prim+br_druge-objects['prim'])*objects['prim_cij']*objects.uspostava
	else:
		if br_prim <= objects['prim'] or objects['prim'] == 1:
			prim_sum = 0
		else:
			prim_sum = (br_prim-objects['prim'])*objects['prim_cij']*objects.uspostava
		if br_druge <= objects['druge'] or objects['druge'] == 1:
			druge_sum = 0
		else:
			druge_sum = (br_druge-objects['druge'])*objects['druge_cij']*objects.uspostava
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

data = []
json_data = open('data.json')
data = json.load(json_data)

# br = len(Racun.objects.all())
# rn = Racun.objects.all()[br]

rez=[]
for x in range(0, len(data)):
	for y in range(0, len(data[x]['tarife'])):
		a_min = 99999
		a = izracun(100, 150, 50, 2, 25, x, y)
		if a<a_min:
			a_min = format(round(a, 2), '.2f')
			tarifa = data[x]['tarife'][y]['ime_tarife']
	rez.append(data[x]['tarife'])
	rez.append(tarifa)
	rez.append(a_min)
	
print(rez)

json_data.close()