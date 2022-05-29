from socket import fromshare
from django.shortcuts import render
# from django import forms
# from .models import Image
# Create your views here.
# from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image
from subprocess import run, PIPE
import sys
import os

# Create your views here.
def inpainting(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            # print(type())
            c=str(form.files['image'])
            print(c)
            out=run([sys.executable,'classify.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)
            if out.stdout.decode()==True:
                inpaint=run([sys.executable,'../aot/src/demo.py' ,'--dir_image' , 'media/img/'+c  ,'--pre_train' ,'../aot/experiments/face/G0000000.pt' , '--painter' ,'bbox'],shell=False,stdout=PIPE)
            else:
                inpaint=run([sys.executable,'../aot/src/demo.py' ,'--dir_image' , 'media/img/'+c  ,'--pre_train' ,'../aot/experiments/place/G0000000.pt' , '--painter' ,'bbox'],shell=False,stdout=PIPE)

            # print(out.stdout.decode())
            obj.image="img/inpaint.png"
            os.remove('media/img/'+c)
            return render(request,"inpaint_result.html",{"obj":obj})

    else:
        form=ImageForm()
        
    img=Image.objects.all()
    
    return render(request,"inpaint.html",{"img":img,"form":form})

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def super_res(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            # print(type())
            c=str(form.files['image'])
            print(c)
            super_resolution=run([sys.executable,'../super/super.py' ,c ],shell=False,stdout=PIPE)
            obj.image="img/output.jpg"
            os.remove('media/img/'+c)
            return render(request,"super_result.html",{"obj":obj})

    else:
        form=ImageForm()
        
    img=Image.objects.all()
    
    return render(request,"inpaint.html",{"img":img,"form":form})
