from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import IhaForm
from .models import Iha
from django.contrib import messages
# Create your views here.

def ihas(request):
    
    keyword=request.GET.get("keyword")
    
    if keyword:
        ihas = Iha.objects.filter(marka__contains=keyword)
        return render(request,"ihas.html",{"ihas":ihas})
    ihas=Iha.objects.all()
    return render(request,"ihas.html",{"ihas":ihas})
    
def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    ihas=Iha.objects.filter(author=request.user)
    context={
        "ihas":ihas
    }
    
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addIha(request):
    form = IhaForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        iha=form.save(commit=False)
        iha.author= request.user
        iha.save()
        messages.success(request,"Ürün Eklendi")
        return redirect("iha:dashboard")
    return render(request,"addiha.html",{"form":form})


def detail(request,id):
    #article =Article.objects.filter(id=id).first
    iha=get_object_or_404(Iha,id=id)
    return render(request,"detail.html",{"iha":iha})

@login_required(login_url = "user:login")

def updateIha(request,id):
    
    article =get_object_or_404(Iha,id=id)
    form = IhaForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        iha=form.save(commit=False)
        iha.author= request.user
        iha.save()
        messages.success(request,"Ürün başarıyla GÜncellendi")
        return redirect("iha:dashboard")
        
    return render(request,"update.html",{"form":form})


def deleteIha(request,id):
    iha=get_object_or_404(Iha,id=id)
    
    iha.delete()
    messages.success(request,"Ürün Silindi..")
    return redirect("iha:dashboard")
    
    
    
    
    