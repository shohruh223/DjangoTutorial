from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app.models import QRCode


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        QRCode.objects.create(name=name)
        return redirect('/')

    qrs = QRCode.objects.all()

    return render(request, 'app/index.html', {'qrs':qrs})