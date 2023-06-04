from django.shortcuts import render, redirect
from twilio.rest import Client


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


