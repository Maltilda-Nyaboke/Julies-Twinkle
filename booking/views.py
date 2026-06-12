from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import BookingForm
from .models import Booking


def home(request):
    return render(request, 'booking/index.html')


def products(request):
    return render(request, 'booking/products.html')


def services(request):
    return render(request, 'booking/services.html')


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = Booking.objects.create(**form.cleaned_data)
            _send_booking_emails(booking)
            return render(request, 'booking/booking_confirmation.html', {'booking': booking})
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})


def _send_booking_emails(booking: Booking) -> None:
    customer_subject = 'Barb Barbershop booking request received'
    customer_message = (
        f'Hi {booking.name},\n\n'
        f'Thanks for booking {booking.service} at Barb Barbershop.\n'
        f'We received your request for {booking.preferred_datetime}.\n\n'
        'We will confirm your exact appointment time shortly.\n\n'
        'Booking details:\n'
        f'  Service: {booking.service}\n'
        f'  Date / time: {booking.preferred_datetime}\n'
        f'  Phone: {booking.phone}\n'
        f'  Notes: {booking.message or "None"}\n\n'
        'If you need to update anything, reply to this email or call us.\n\n'
        'Barb Barbershop'
    )

    shop_subject = 'New Barb Barbershop booking request'
    shop_message = (
        'New booking request received.\n\n'
        f'Name: {booking.name}\n'
        f'Email: {booking.email}\n'
        f'Phone: {booking.phone}\n'
        f'Service: {booking.service}\n'
        f'Preferred date / time: {booking.preferred_datetime}\n'
        f'Notes: {booking.message or "None"}\n\n'
        'Confirm the appointment with the customer as soon as possible.'
    )

    send_mail(
        customer_subject,
        customer_message,
        settings.DEFAULT_FROM_EMAIL,
        [booking.email],
        fail_silently=False,
    )

    send_mail(
        shop_subject,
        shop_message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.SHOP_BOOKING_EMAIL],
        fail_silently=False,
    )
