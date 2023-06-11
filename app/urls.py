from django.urls import path

from app.views import index, CreateNew

urlpatterns = [
    path('', index, name='index'),
    path('new/', CreateNew.as_view(), name='new')
]