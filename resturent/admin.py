from django.contrib import admin
from .models import Resturent

# Register your models here.


@admin.register(Resturent)
class ResturentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'booking_status']
    list_filter = ['booking_status']

