from django.urls import path

from app.views import index

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', index, name='index'),
]