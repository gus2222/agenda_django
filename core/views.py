from django.shortcuts import render, HttpResponse
from core.models import Evento
# Create your views here.

def eventos(request, titulo_evento):
    local = Evento.objects.get(titulo = titulo_evento).descricao
    return HttpResponse('<h2>O local do Evento {} é {} </h2>'.format(titulo_evento,local))