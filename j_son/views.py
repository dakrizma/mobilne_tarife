from django.shortcuts import render

def input(request):
	rez = 2
	return render(request, 'j_son/input.html', {'rez': rez})