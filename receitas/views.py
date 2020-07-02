from django.shortcuts import render, HttpResponse, redirect
from .forms import ReceitaForm

# Create your views here.
def receitas(request):
    return HttpResponse('Módulo de receitas')

def receitas_create(request):
    form = ReceitaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('receitas')    

    return render(request, 'form.html', {'form': form})
