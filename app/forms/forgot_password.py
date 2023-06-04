from django.core.exceptions import ValidationError
from django.forms import Form, EmailField

from app.models import User


class ForgotPasswordForm(Form):
    email = EmailField()

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('Not email found with this email.')
        return email