from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_superuser', 'acc_type']
    list_filter = ['acc_type']
from django.contrib import admin

# Register your models here.
