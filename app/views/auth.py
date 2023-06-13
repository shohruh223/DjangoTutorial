from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from app.forms.login import LoginForm
from app.forms.register import RegisterForm
from app.forms.send_email_form import send_email, send_forget_password_mail
from app.models import User


def is_user_authenticated(user):
    return user.is_authenticated


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                send_email(form.data.get('email'), request, 'register')
                messages.add_message(
                    request=request,
                    level=messages.WARNING,
                    message="Successfully send your email, please activate your profile"
                )
                return redirect('register')
        else:
            form = RegisterForm()
    return render(request, 'app/register.html', {"form":form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('index')
        else:
            form = LoginForm()
    return render(request, 'app/login.html', {"form":form})


@login_required(login_url='login')
def forget_password(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')

            if not User.objects.filter(email=email).first():
                messages.success(request, 'Not email found with this email.')
                return redirect('forgot_password')

            user = User.objects.get(email=email)
            send_forget_password_mail(email=user, request=request)
            messages.success(request, 'Successfully send your email, please change your password')
            return redirect('forgot_password')

    except Exception as e:
        print(e)
    return render(request, 'app/forgot_password.html')


@login_required(login_url='login')
def change_password(request):
    user_id = request.user.id
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if user_id is None:
            messages.success(request, 'User is not found')
            return redirect('forget_password')

        if new_password != confirm_password:
            messages.success(request, 'both should be equal')
            return redirect('change_password')

        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
        return redirect('login')
    return render(request, 'app/change_password.html')


@login_required(login_url='index')
def logout_view(request):
    logout(request)
    return render(request, 'app/logout.html')