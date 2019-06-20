from django.shortcuts import render
import requests
import json
from .forms import Form

# Create your views here.

def home(request):
    
    try:
        obj=requests.get("http://ipinfo.io")
        g=True
    except Exception as e:
        g=False
        status="no"
        obj={}

    # obj='{"bla":2,"status_code":200}'
    if(g and obj.status_code == 200 ):
        obj=json.loads(obj.text)
        status="yes"

    else:
        status="no"

    return render(request,'home.html',{"obj":obj,"status":status})


def search(request):

    if (request.method=="POST"):

        form=Form(request.POST)
        print(form)

        if(form.is_valid):
            ip=form.cleaned_data['ip']

            try:
                obj=requests.get("http://ipinfo.io/"+ip)
                g=True
            except Exception as e:
                g=False
                status="no"
                obj={}

            if(g and obj.status_code == 200):
                obj=json.loads(obj.text)
                status="yes"
            else:
                status="no"
  

            return render(request,'home.html',{"obj":obj,"status":status})


    else:
        form=Form()

    return render(request,'search.html',{"form":form})

