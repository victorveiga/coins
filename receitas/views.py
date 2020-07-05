from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReceitaForm
from .models import Receita

# Create your views here.
@login_required
def receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'list.html', {'receitas': receitas})

@login_required
def receitas_create(request):
    form = ReceitaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('receitas')    

    return render(request, 'form.html', {'form': form})

@login_required
def receitas_update(request, id):
    receita = get_object_or_404(Receita, pk=id)
    form = ReceitaForm(request.POST or None, request.FILES or None, instance=receita)

    if form.is_valid():
        form.save()
        return redirect('receitas')    

    return render(request, 'form.html', {'form': form})    
