
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def show_post(request):
    return render(request,'show_post.html')
