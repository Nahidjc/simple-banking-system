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
    if request.method == 'POST':
        senderEmail = request.POST.get('senderEmail')
        receiverEmail = request.POST.get('receiverEmail')
        transferBalance = request.POST.get('transferBalance')
        print(senderEmail, receiverEmail, transferBalance)
        senderPreviousBalance = registerUser.objects.get(
            email=senderEmail).balance
        receiverPreviousBalance = registerUser.objects.get(
            email=receiverEmail).balance
        print(senderPreviousBalance, receiverPreviousBalance)

        if int(senderPreviousBalance) >= int(transferBalance):
            updateSenderBalance = int(
                senderPreviousBalance)-int(transferBalance)
            updateReceiverBalance = int(
                receiverPreviousBalance)+int(transferBalance)
            print(updateSenderBalance, updateReceiverBalance)

            # transaction history
            history = transferAmount()
            history.sender = senderEmail
            history.receiver = receiverEmail
            history.transfer_amount = int(transferBalance)
            history.save()

            # update balance
            registerUser.objects.filter(
                email=senderEmail).update(balance=updateSenderBalance)
            registerUser.objects.filter(
                email=receiverEmail).update(balance=updateReceiverBalance)

    return render(request, 'banking/home.html', )
