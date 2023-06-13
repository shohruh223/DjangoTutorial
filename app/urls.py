from django.urls import path
from app.views.activate_mail import ActivateEmailView, ActivatePasswordEmailView
from app.views.auth import login_view, register, change_password, forget_password, logout_view
from app.views.index import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('activate/<str:uid>/<str:token>', ActivateEmailView.as_view(), name='confirm-mail'),
    path('forgot-password/', forget_password, name='forgot_password'),
    path('activate_password/<str:uid>/<str:token>', ActivatePasswordEmailView.as_view(), name='activate_password'),
    path('change-password/', change_password, name='change_password')
]