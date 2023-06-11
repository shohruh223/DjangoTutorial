from django import forms

from app.models import User


class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ()