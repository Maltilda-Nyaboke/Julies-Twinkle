from django.db import models

SERVICE_CHOICES = [
    ('haircut', 'Haircut'),
    ('shave', 'Shave'),
    ('beard', 'Beard Trim'),
    ('combo', 'Haircut + Beard'),
]

class Booking(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    preferred_datetime = models.CharField(max_length=120)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.name} — {self.service} on {self.preferred_datetime}'
