from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from app.form import UserModelForm
from app.models import User


def index_view(request):
    users = User.objects.order_by('-id')
    return render(request, 'app/index.html', {'users':users})


def detail_view(request, user_id):
    user = User.objects.filter(id=user_id).first()
    context = {
        "user":user
    }
    return render(request, 'app/details.html', context)


def create_view(request):
    if request.method == "POST":
        form = UserModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserModelForm()
    context = {
        "form":form
    }
    return render(request, 'app/create_user.html', context)


def update_view(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if request.method == "POST":
        form = UserModelForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserModelForm(instance=user, initial={"image":user.image,
                                                 "fullname":user.fullname,
                                                 "address":user.address,
                                                 "age":user.age}
                         )
    context = {
        "form":form,
        "user":user
    }
    return render(request, 'app/edit_user.html', context)


def delete_user_view(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if user:
        user.delete()
    return redirect('index')






