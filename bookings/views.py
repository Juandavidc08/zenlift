from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Trainer, Appointment
from .forms import AppointmentForm
from django.contrib import messages

# List of Trainers
def trainers_list(request):
    trainers = Trainer.objects.all()  # Fetch all trainers
    return render(request, 'bookings/trainers_list.html', {'trainers': trainers})

# Book an Appointment
@login_required
def book_appointment(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)  # Get the selected trainer
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Link the user to the appointment
            appointment.trainer = trainer  # Assign the trainer automatically
            appointment.save()
            messages.success(request, 'Your appointment has been successfully booked!')
            return redirect('appointment_confirmation', appointment_id=appointment.id)
    else:
        # Pre-fill the form with the selected trainer
        form = AppointmentForm(initial={'trainer': trainer})

    return render(request, 'bookings/book_appointment.html', {'form': form, 'trainer': trainer})

# Appointment Confirmation
def appointment_confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)  # Get the appointment details
    return render(request, 'bookings/appointment_confirmation.html', {'appointment': appointment})
