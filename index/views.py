from django.shortcuts import render, redirect
from .models import Cats, Dogs, Hamsters
from django.views import View

# Create your views here.
def home_page(request):
    viewcats = Cats.objects.all()
    viewdogs = Dogs.objects.all()
    viewhamsters = Hamsters.objects.all()

    context = {'viewcats': viewcats,
               'viewdogs': viewdogs,
               'viewhamsters': viewhamsters}
    return render(request, 'home.html', context)

def view_cats(request):
    viewcats = Cats.objects.all()
    context = {'viewcats': viewcats}
    return render(request, 'cats.html', context)

def view_dogs(request):
    viewdogs = Dogs.objects.all()
    context = {'viewdogs': viewdogs}
    return render(request, 'dogs.html', context)

def view_hamsters(request):
    viewhamsters = Hamsters.objects.all()
    context = {'viewhamsters': viewhamsters}
    return render(request, 'hamsters.html', context)