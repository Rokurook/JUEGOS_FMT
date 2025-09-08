from django.shortcuts import render

# Create your views here.
def menuprincipal_wiki_estatico(request):
    return render(request, 'core/menuprincipal_wiki.html')

def animales(request):
    return render(request, 'core/Animales.html')