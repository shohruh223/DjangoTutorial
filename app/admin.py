from django.contrib import admin

from app.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name')


admin.site.register(User, UserAdmin)
