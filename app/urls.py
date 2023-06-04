from django.urls import path, include
from app.views import index, auth_login, confirm

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_login, name='login'),
    path('confirm/<uuid:id>', confirm, name='confirm'),
]