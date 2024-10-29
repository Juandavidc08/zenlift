from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.

def index(request):
    """A view to return the index page"""
    
    return render(request, 'home/index.html')

def custom_404_view(request, exception):
    return render(request, 'home/404.html', status=404)

def test_email(request):
    try:
        send_mail(
            'Test Email Subject',
            'This is a test email body.',
            'your_email@gmail.com',
            ['recipient_email@example.com'],
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")