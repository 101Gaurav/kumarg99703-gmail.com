from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def home(request):
    return render(request, "firstapp_home.html", {"name": "COVID-19"})



def stats(request):

    cov=models.cov
    return render(request, "covid_stats.html",{"cov":cov})

def searching(request):
    n1=request.POST["n1"]
    for i in models.cov:
        if n1 == i.country:
            return render(request, "result.html", {"res": i})

    else:
        return HttpResponse("not found")