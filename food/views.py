from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def show_pizza(request):
  return render(request, 'food/pizza.html')


def berenjmorgh(request):
  return render(request, 'food/berenjmorg.html')

def hamburger(request):
  return render(request, 'food/hamburger.html')
