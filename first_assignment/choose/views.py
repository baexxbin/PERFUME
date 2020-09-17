from django.shortcuts import render
from .models import Blog

# Create your views here.
def choose(request):
    return render(request,'choose.html')

def choose_atm(request):
    return render(request, 'choose_atm.html')

def choose3(request):
    return render(request,'choose3.html')

def home(request):
    blogs=Blog.objects #전달받은 객체 (쿼리셋) 
    return render(request, 'home.html', {'blogs':blogs})
