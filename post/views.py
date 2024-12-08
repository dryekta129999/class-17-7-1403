from django.db.models.signals import post_save
from django.shortcuts import render
from post.models import Post


# Create your views here.
def show_post(request):
    posts=Post.objects.all()

    # only filters status='Published'
    # posts=Post.objects.filter(status='Published')


    return render(request,'show_post.html',{'posts':posts})
