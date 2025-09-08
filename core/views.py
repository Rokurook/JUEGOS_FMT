from django.shortcuts import render

# Create your views here.
def menuprincipal_wiki_estatico(request):
    return render(request, 'core/menuprincipal_wiki.html')

def animales(request):
    return render(request, 'core/Animales.html')

def foro(request):
    return render(request, 'core/forowiki.html')

def registrarse(request):
    return render(request, 'core/registrase_wiki.html')

def inicio_sesion(request):
    return render(request, 'core/inicio_sesion_wiki.html')

def mi_cuenta(request):
    return render(request, 'core/micuentatf.html')

def Flora(request):
    return render(request, 'core/Flora.html')

def historia(request):
    return render(request, 'core/historia.html')

def armas(request):
    return render(request, 'core/Armas.html')

def construcciones(request):
    return render(request, 'core/Construcciones.html')

def consumibles(request):
    return render(request, 'core/Consumibles.html')

def enemigos(request):
    return render(request, 'core/Enemigos.html')
