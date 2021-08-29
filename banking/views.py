from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def home(request):
    if request.method == 'GET':
        print("paichi")

    return render(request, 'banking/home.html')
