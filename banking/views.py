from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import registerUser, transferAmount
# Create your views here.


def home(request):
    if request.method == 'GET':
        emails = registerUser.objects.only('email')
        print(emails)

    return render(request, 'banking/home.html', context={'emails': emails})


def registerAccount(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        balance = request.POST.get('balance')
        if registerUser.objects.filter(email=email).exists():
            return HttpResponse('<h1>Your email is already in our list of users to be notified.Try a new email</h1>')
        else:
            user = registerUser()
            user.name = name
            user.balance = balance
            user.email = email
            user.save()
            print(user.name, user.email)
    return render(request, 'banking/register.html')


def user_details(request):
    users = registerUser.objects.all()
    print(users)
    return render(request, 'banking/user_details.html', context={'users': users})


def transfer(request):
    # if request.method == 'GET':
    #     email = registerUser.objects.only('email')
    #     print(email)

    return render(request, 'banking/home.html', )
