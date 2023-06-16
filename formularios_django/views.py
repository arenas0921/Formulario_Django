from django.http import HttpResponse
from django.shortcuts import render
from .forms import ComentarioForm, ContactoForm


def form(request):
    comentario_form = ComentarioForm()
    return render(request, 'form.html', {'comentario_form': comentario_form})


def goal(request):
    if request.method != 'GET':
        return HttpResponse("metodo no permitido")

    return HttpResponse(request.GET['nombre'])


def widget(request):
    if request.method == 'GET':
        form = ContactoForm()
        return render(request, 'widget.html', {'form': form})

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valido")
        else:
            return render(request, 'widget.html', {'form': form})