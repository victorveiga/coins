from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
def sigin(request):
    form = UserForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'registration/register.html', {'form': form})

@login_required
def update_user(request, id):
    user = get_object_or_404(User, pk=id)

    form = UserForm(request.POST or None, request.FILES or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'registration/register.html', {'form': form})


@login_required
def logout_now(request):
    logout(request)
    return redirect('home')
