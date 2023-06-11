from django.urls import path
from django.views.generic import DetailView

from app.views import index_view, detail_view, create_view, update_view, delete_user_view

urlpatterns = [
    path('', index_view, name='index'),
    path('details/<int:user_id>', detail_view, name='details'),
    path('create-user/', create_view, name='create-user'),
    path('edit-user/<int:user_id>', update_view, name='edit-user'),
    path('delete-user/<int:user_id>', delete_user_view, name='delete-user'),
]