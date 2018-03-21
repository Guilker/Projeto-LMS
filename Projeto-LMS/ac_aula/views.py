# views.py

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contato(request):

    if request.method == 'GET':
        return render(request, 'contato.html')

    if request.method == 'POST':
        login=request.POST['login']
        senha=request.POST['senha']
        return HttpResponse("<center>Usuario: %s, e senha: %s foi digitada.!</center>" % (login,senha))

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':

        senha=request.POST['senha']
        login=request.POST['login']
        
        if senha == 'teste123':
            return render(request, 'login.html')
        else:
            return HttpResponse("<center>Usuario %s,  digitou a senha errada!</center>" % login)
            
    