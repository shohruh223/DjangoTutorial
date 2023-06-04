from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.forms.forgot_password import ForgotPasswordForm
from app.forms.login import LoginForm
from app.forms.register import RegisterForm
from app.forms.send_email_form import send_email, send_forget_password_mail
from app.models import User


# class LoginMixin:
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('index')
#         return super().get(self,request, *args, **kwargs)


class RegisterPage(FormView):
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        form.save()
        send_email(form.data.get('email'), self.request, 'register')
        messages.add_message(
            self.request,
            level=messages.WARNING,
            message='Successfully send your email, please activate your profile'
        )
        return super().form_valid(form)


class LoginPage(LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)


# class ForgotPassword(FormView):
#     form_class = ForgotPasswordForm
#     template_name = 'app/forgot_password.html'
#     success_url = reverse_lazy('forget_password')
#
#     def form_valid(self, form):
#         send_email(form.data.get('email'), self.request, 'forgot_password')
#         messages.add_message(
#             self.request,
#             level=messages.WARNING,
#             message='Successfully send your email, Not email found with this email.'
#         )
#         return super().form_valid(form)

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


def logout_view(request):
    logout(request)
    return render(request, 'app/logout.html')