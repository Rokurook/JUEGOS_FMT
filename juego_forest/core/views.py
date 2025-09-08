from django.shortcuts import render

# Create your views here.
def menuprincipal_wiki_estatico(request):
    return render(request, 'menuprincipal_wiki.html')
