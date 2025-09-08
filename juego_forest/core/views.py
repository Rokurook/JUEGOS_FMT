from django.shortcuts import render

# Create your views here.
def menuprincipal_wiki(request):
    return render(request, menuprincipal_wiki.html)