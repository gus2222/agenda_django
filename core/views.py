from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# def index(request):
#     return redirect("/agenda/")

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("/")

def submit_login(request):
    if request.POST:
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("/")
        else:
            messages.error(request, "Usuário ou Senha Inválido")
    return  redirect("/")

@login_required(login_url="/login/")
def lista_eventos(request):
    usuario = request.user
    #evento = Evento.objects.all()
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)

def eventos(request, titulo_evento):
    local = Evento.objects.get(titulo = titulo_evento).descricao
    return HttpResponse('<h2>O local do Evento {} é {} </h2>'.format(titulo_evento,local))