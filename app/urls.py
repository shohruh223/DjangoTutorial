from django.urls import path, include

from app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]