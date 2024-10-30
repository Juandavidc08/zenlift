from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    send_mail("Welcome!", "Thank you for signing up.", [user.email])
