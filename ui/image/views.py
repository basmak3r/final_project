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

# Create your views here.
def super1(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            # print(type())
            c=str(form.files['image'])
            print(c)
            # out=run([sys.executable,'classify.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)
            # if out==True : 
                # out=run([sys.executable,'inpaint.py' ,'cordinate' , 'face'+c],shell=False,stdout=PIPE)
            # inpaint=run([sys.executable,'../aot/src/demo.py' ,'--x1' ,'100', '--y1', '200' ,'--x2' ,'300' ,'--y2', '100' ,'--dir_image' , 'media/img/'+c  ,'--pre_train' ,'../aot/experiments/G0000000.pt' , '--painter' ,'bbox'],shell=False,stdout=PIPE)
            inpaint=run([sys.executable,'../aot/src/demo.py' ,'--dir_image' , 'media/img/'+c  ,'--pre_train' ,'../aot/experiments/G0000000.pt' , '--painter' ,'bbox'],shell=False,stdout=PIPE)

            # else:
            #     out=run([sys.executable,'inpaint.py' ,'cordinate' , 'place'+c],shell=False,stdout=PIPE)
            
            # out=run([sys.executable,'superresolution.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)
            # out=run([sys.executable,'classify.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)

            # print(out.stdout.decode())
            obj.image="img/1.png"
            print(obj.image)
            return render(request,"inpaint.html",{"obj":obj})

    else:
        form=ImageForm()
        
    img=Image.objects.all()
    
    # print(out.stdout.decode())
    return render(request,"super.html",{"img":img,"form":form})

def index(request):
    return render(request,"index.html")



def super2(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            # print(type())
            c=str(form.files['image'])
            # print(c)
            # out=run([sys.executable,'classify.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)
            # print(out)
            # if out==True : 
                # out=run([sys.executable,'inpaint.py' ,'cordinate' , 'face'+c],shell=False,stdout=PIPE)
            # inpaint=run([sys.executable,'../aot/src/demo.py' ,'--x1' ,'100', '--y1', '200' ,'--x2' ,'300' ,'--y2', '100' ,'--dir_image' , 'media/img/'+c  ,'--pre_train' ,'../aot/experiments/G0000000.pt' , '--painter' ,'bbox'],shell=False,stdout=PIPE)
            inpaint=run([sys.executable,'../aot/src/demo.py' ,'--dir_image' , 'media/img/'+c  ,'--pre_train' ,'../aot/experiments/G0000000.pt' , '--painter' ,'bbox'],shell=False,stdout=PIPE)

            # else:
            #     out=run([sys.executable,'inpaint.py' ,'cordinate' , 'place'+c],shell=False,stdout=PIPE)
            
            # out=run([sys.executable,'superresolution.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)
            # out=run([sys.executable,'classify.py' ,'--image1' , 'media/img/'+c],shell=False,stdout=PIPE)

            # print(out.stdout.decode())
            obj.image="img/1.png"
            print(obj.image)
            return render(request,"inpaint.html",{"obj":obj})

    else:
        form=ImageForm()
        
    img=Image.objects.all()
    
    # print(out.stdout.decode())
    return render(request,"super.html",{"img":img,"form":form})