from django.shortcuts import render

def IniciarSesion(request):
	return render(request, 'index.html', {})

def MuroGeneral(request):
	return render(request, 'murogeneral.html', {})

def Perfil(request):
	return render(request, 'perfil.html', {})

def Registrarse(request):
	return render(request, 'registrarse.html', {})
