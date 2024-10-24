from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Trainer, Appointment
from .forms import AppointmentForm
from django.contrib import messages

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# List of Trainers
def trainers_list(request):
    trainers = Trainer.objects.all()  # Fetch all trainers
    return render(request, 'bookings/trainers_list.html', {'trainers': trainers})

# Book an Appointment
@login_required
def book_appointment(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.trainer = trainer
            appointment.save()

            # Redirect to the payment page
            return redirect('payment', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    return render(request, 'bookings/book_appointment.html', {'form': form, 'trainer': trainer})


@login_required
def payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        # Create a Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'Appointment with {appointment.trainer.name}',
                    },
                    'unit_amount': 5000,  # $50 in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('payment_success', args=[appointment.id])
            ),
            cancel_url=request.build_absolute_uri(
                reverse('payment_cancel')
            ),
        )

        return redirect(session.url, code=303)

    return render(request, 'bookings/payment.html', {'appointment': appointment})


@login_required
def payment_success(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.payment_status = True  # Mark the appointment as paid
    appointment.save()
    
    messages.success(request, 'Payment successful! Your appointment is confirmed.')
    return redirect('appointment_confirmation', appointment_id=appointment.id)


@login_required
def payment_cancel(request):
    messages.error(request, 'Payment was canceled. Please try again.')
    return redirect('trainers_list')


# Appointment Confirmation
def appointment_confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)  # Get the appointment details
    return render(request, 'bookings/appointment_confirmation.html', {'appointment': appointment})
