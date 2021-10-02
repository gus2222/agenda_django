from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.

# def index(request):
#     return redirect("/agenda/")

def lista_eventos(request):
    usuario = request.user
    ##evento = Evento.objects.all()
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)

def eventos(request, titulo_evento):
    local = Evento.objects.get(titulo = titulo_evento).descricao
    return HttpResponse('<h2>O local do Evento {} é {} </h2>'.format(titulo_evento,local))