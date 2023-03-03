from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import Actor
# Create your views here.





#
# def demo(request):
#
#   return  render(request,'index.html')

def home(request):
  place=Place.objects.all()
  actor = Actor.objects.all()
  return render(request,"index.html",{'place':place,'actor':actor})

# def insta(request):
#
#   return render(request,"index.html",})