from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import render, redirect
from twilio.rest import Client
from random import randint

from app.models import User


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        if text:
            account_sid = "your account_sid"
            auth_token = "your auth_token"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                to="+998334530919",
                from_="+13613093414",
                body=f"Sizga {name} SMS jo'natdi: {text}")
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'app/index.html')


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            confirm = user.confirm = randint(10_000, 99_999)
            user.save()
            messages.warning(request, 'Success')
            send_sms(body="Your activation code: " + str(confirm), number=user.phone_number)
            return redirect('confirm', user.id)
        else:
            messages.warning(request, 'Wrong details, please try again')
            return redirect('login')

    return render(request, 'app/login.html')


def confirm(request, id):
    if not request.user.is_authenticated:
        user = User.objects.get(id=id)
        if user and user.confirm != 0:
            if request.method == 'POST':
                confirm = request.POST['confirm']
                if user.confirm == int(confirm):
                    login(request, user)
                    user.confirm = 0
                    user.save()
                    return redirect('/')
                else:
                    messages.warning(request, 'Wrong !!')
        else:
            return redirect('/')
    else:
        return redirect('/')

    return render(request, 'app/confirm.html', {'user':user})


def send_sms(body, number):
    account_id = "your account_id"
    auth_token = "your auth_token"
    client = Client(account_id, auth_token)
    messages = client.messages.create(
        body=body,
        from_='+13613093414',
        to=number
    )



