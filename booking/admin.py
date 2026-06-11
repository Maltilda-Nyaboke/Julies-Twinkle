from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'preferred_datetime', 'email', 'phone', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
