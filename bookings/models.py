from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    payment_status = models.BooleanField(default=False)  # New field to track payment

    def __str__(self):
        return f"{self.user.username} - {self.trainer.name} on {self.date} at {self.time}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='booking_profile')
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=False, blank=False, default='US')

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bookings')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"Booking {self.id} - {self.appointment.trainer.name} for {self.user_profile.user.username}"
